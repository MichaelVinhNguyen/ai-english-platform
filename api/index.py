import os
import sys
import traceback
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

try:
    from backend.main import app

    class VercelPathMiddleware:
        def __init__(self, asgi_app):
            self.asgi_app = asgi_app

        async def __call__(self, scope, receive, send):
            if scope["type"] == "http":
                headers = dict(scope.get("headers", []))
                forwarded = headers.get(b"x-forwarded-uri", b"").decode("utf-8") or headers.get(b"x-matched-path", b"").decode("utf-8")
                if forwarded:
                    clean_path = forwarded.split("?")[0]
                    if not clean_path.startswith("/api") and clean_path != "/":
                        clean_path = "/api" + clean_path
                    scope["path"] = clean_path
            await self.asgi_app(scope, receive, send)

    handler = VercelPathMiddleware(app)
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    app = FastAPI()
    err_tb = traceback.format_exc()
    @app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def catch_import_error(full_path: str = ""):
        return JSONResponse(status_code=500, content={"error": "Backend import failed", "detail": str(e), "traceback": err_tb})
    handler = app
