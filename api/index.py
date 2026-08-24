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
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    app = FastAPI()
    err_tb = traceback.format_exc()
    @app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def catch_import_error(full_path: str = ""):
        return JSONResponse(status_code=500, content={"error": "Backend import failed", "detail": str(e), "traceback": err_tb})

# Export handler for Vercel
handler = app
