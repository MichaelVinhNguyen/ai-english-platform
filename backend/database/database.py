"""
database.py – Database engine & session management
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from backend.config import settings


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    connect_args={"check_same_thread": False},
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def init_db():
    """Create all tables."""
    async with engine.begin() as conn:
        from backend.database import models  # noqa: F401
        await conn.run_sync(Base.metadata.create_all)
        
    # Seed default admin users
    from sqlalchemy import select
    from backend.database.models import User
    from backend.routers.auth import hash_password
    
    async with AsyncSessionLocal() as session:
        # VihTech Admin
        result = await session.execute(select(User).where(User.username == "VihTech"))
        admin_user = result.scalar_one_or_none()
        if not admin_user:
            admin_user = User(
                email="admin@vihtech.com",
                username="VihTech",
                full_name="VihTech Admin",
                password_hash=hash_password("vihtech2026"),
                role="admin",
                is_active=True
            )
            session.add(admin_user)
            await session.commit()
            print("[OK] Admin user 'VihTech' created.")

        # Default Admin (admin / admin123)
        result2 = await session.execute(select(User).where(User.username == "admin"))
        admin2 = result2.scalar_one_or_none()
        if not admin2:
            admin2 = User(
                email="admin@example.com",
                username="admin",
                full_name="Administrator",
                password_hash=hash_password("admin123"),
                role="admin",
                is_active=True
            )
            session.add(admin2)
            await session.commit()
            print("[OK] Admin user 'admin' created.")

        # Admin users created cleanly
        pass


async def get_db():
    """Dependency – yield AsyncSession."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
