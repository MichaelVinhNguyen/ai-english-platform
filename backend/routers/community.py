from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.database import get_db
from backend.database.models import User, Post, Comment
from backend.database.schemas import PostCreate, CommentCreate
from backend.routers.auth import get_current_user

community_router = APIRouter(prefix="/api/community", tags=["Community"])

@community_router.get("/posts")
async def get_posts(category: Optional[str] = None, limit: int = 20,
                     db: AsyncSession = Depends(get_db),
                     current_user: User = Depends(get_current_user)):
    q = select(Post, User.username, User.avatar_url).join(User, Post.user_id == User.id)
    if category: q = q.where(Post.category == category)
    r = await db.execute(q.order_by(desc(Post.created_at)).limit(limit))
    return [{"id": p.id, "title": p.title, "content": p.content[:200],
             "category": p.category, "likes": p.likes, "created_at": p.created_at,
             "username": username, "avatar_url": avatar}
            for p, username, avatar in r.all()]

@community_router.post("/posts")
async def create_post(data: PostCreate, db: AsyncSession = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    post = Post(user_id=current_user.id, title=data.title,
                content=data.content, category=data.category)
    db.add(post)
    await db.commit()
    return {"id": post.id, "title": post.title, "message": "Đăng bài thành công!"}

@community_router.get("/posts/{post_id}")
async def get_post(post_id: int, db: AsyncSession = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    r = await db.execute(select(Post).where(Post.id == post_id))
    post = r.scalar_one_or_none()
    if not post: return {"error": "Post not found"}
    r2 = await db.execute(select(Comment, User.username)
                           .join(User, Comment.user_id == User.id)
                           .where(Comment.post_id == post_id))
    comments = [{"id": c.id, "content": c.content, "likes": c.likes,
                 "created_at": c.created_at, "username": u} for c, u in r2.all()]
    return {"id": post.id, "title": post.title, "content": post.content,
            "category": post.category, "likes": post.likes,
            "created_at": post.created_at, "comments": comments}

@community_router.post("/posts/{post_id}/comments")
async def add_comment(post_id: int, data: CommentCreate,
                       db: AsyncSession = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    comment = Comment(post_id=post_id, user_id=current_user.id, content=data.content)
    db.add(comment)
    await db.commit()
    return {"message": "Đã thêm bình luận"}
