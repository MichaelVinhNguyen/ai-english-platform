import os
import sys
import traceback
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Flag Vercel environment
os.environ["VERCEL"] = "1"

# Copy pre-seeded database if on Vercel
try:
    tmp_db = Path("/tmp/app.db")
    bundled_db = BASE_DIR / "data" / "app.db"
    if not tmp_db.exists() and bundled_db.exists():
        import shutil
        shutil.copy2(bundled_db, tmp_db)
        print("[VERCEL INIT] Copied pre-seeded database to /tmp/app.db")
except Exception as e:
    print(f"[VERCEL INIT ERROR] {e}")

try:
    from backend.main import app as fastapi_app

    class VercelRoutingMiddleware:
        def __init__(self, app):
            self.app = app

        async def __call__(self, scope, receive, send):
            if scope["type"] == "http":
                path = scope.get("path", "")
                # Normalize path if Vercel stripped /api
                if not path.startswith("/api") and path != "/":
                    scope["path"] = "/api" + (path if path.startswith("/") else "/" + path)
            await self.app(scope, receive, send)

    handler = VercelRoutingMiddleware(fastapi_app)
except Exception as exc:
    err_tb = traceback.format_exc()
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    fallback = FastAPI()
    
    @fallback.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"])
    async def fallback_error_handler(full_path: str = ""):
        return JSONResponse(
            status_code=500,
            content={
                "error": "Serverless Function Failed To Initialize",
                "detail": str(exc),
                "traceback": err_tb
            }
        )
    handler = fallback

app = handler


