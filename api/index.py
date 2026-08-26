import os
import sys
import shutil
import urllib.parse
import traceback
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Ensure database is copied to /tmp/app.db if running on Vercel
src_db = BASE_DIR / "data" / "app.db"
tmp_db = Path("/tmp/app.db")
try:
    if src_db.exists():
        tmp_db.parent.mkdir(parents=True, exist_ok=True)
        if not tmp_db.exists() or tmp_db.stat().st_size < 100000:
            shutil.copyfile(str(src_db), str(tmp_db))
except Exception as e:
    print("[WARN] Vercel DB sync error:", e)

try:
    from backend.main import app

    class VercelPathMiddleware:
        def __init__(self, asgi_app):
            self.asgi_app = asgi_app

        async def __call__(self, scope, receive, send):
            if scope["type"] == "http":
                path = scope.get("path", "")
                headers = dict(scope.get("headers", []))
                
                # 1. Check x-forwarded-uri first
                raw_uri = headers.get(b"x-forwarded-uri", b"").decode("utf-8")
                if raw_uri and "index.py" not in raw_uri:
                    path = raw_uri.split("?")[0]
                elif "index.py" in path:
                    # 2. Check x-now-route-matches (e.g. 1=level-curriculum/detail/B1)
                    route_matches = headers.get(b"x-now-route-matches", b"").decode("utf-8")
                    if route_matches:
                        for part in route_matches.split("&"):
                            if part.startswith("1="):
                                matched_subpath = urllib.parse.unquote(part[2:])
                                path = "/api/" + matched_subpath.lstrip("/")
                                break
                    else:
                        matched = headers.get(b"x-matched-path", b"").decode("utf-8")
                        if matched and "index.py" not in matched:
                            path = matched.split("?")[0]

                if not path.startswith("/"):
                    path = "/" + path

                # Clean any duplicate /api/api
                while path.startswith("/api/api/"):
                    path = "/api/" + path[9:]

                # If path does not start with /api and is not root /, ensure /api prefix
                if not path.startswith("/api") and path != "/":
                    path = "/api" + path

                # Clean trailing /index.py
                if path.endswith("/index.py"):
                    path = path[:-9]
                    if not path:
                        path = "/api/health"

                scope["path"] = path

            await self.asgi_app(scope, receive, send)

    handler = VercelPathMiddleware(app)
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    app = FastAPI()
    err_tb = traceback.format_exc()

    @app.get("/api/health")
    @app.get("/api/debug")
    async def debug_err():
        return JSONResponse({"status": "error", "traceback": err_tb}, status_code=500)

    handler = app

app = handler

