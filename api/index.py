import os
import sys
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

from backend.main import app

