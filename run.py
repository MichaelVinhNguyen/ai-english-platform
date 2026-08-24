# -*- coding: utf-8 -*-
"""
run.py – Trinh khoi dong ung dung AI English Learning Platform cuc bo (Local Server)
Toi uu hoa 100% cho Windows: Tu dong giai phong cong cu, kiem tra thu vien va mo trinh duyet.
"""
import os
import sys

# Force UTF-8 stdout/stderr on Windows to avoid cp1252 charmap encode errors
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import time
import socket
import subprocess
import webbrowser

def free_port(port: int):
    """Giai phong cong neu co tien trinh zombie cu dang chiem giu."""
    try:
        res = subprocess.run(f'netstat -ano | findstr :{port}', shell=True, capture_output=True, text=True)
        if res.stdout:
            for line in res.stdout.strip().split('\n'):
                parts = line.strip().split()
                if len(parts) >= 5 and f':{port}' in parts[1] and parts[3] == 'LISTENING':
                    pid = parts[4]
                    if pid and pid != '0' and int(pid) != os.getpid():
                        print(f"[DON DEP] Dang giai phong cong {port} tu tien trinh cu (PID: {pid})...")
                        subprocess.run(f'taskkill /F /PID {pid}', shell=True, capture_output=True)
                        time.sleep(0.6)
    except Exception:
        pass

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def find_available_port(start_port: int = 8000) -> int:
    port = start_port
    while is_port_in_use(port) and port < start_port + 20:
        port += 1
    return port

def ensure_dependencies():
    """Kiem tra va tu dong cai dat cac thu vien thiet yeu neu thieu."""
    required = ["fastapi", "uvicorn", "sqlalchemy", "aiosqlite", "dotenv", "pydantic"]
    missing = []
    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    
    if missing:
        print(f"[CAI DAT] Dang tu dong cai dat thu vien: {', '.join(missing)}...")
        subprocess.run([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn", "sqlalchemy", "aiosqlite", "python-dotenv", "pydantic", "requests", "-q"])
        print("[OK] Da cai dat xong thu vien!")

def main():
    # Set current directory to script location
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("=" * 64)
    print("      AI ENGLISH LEARNING PLATFORM - VIHTECH 2026")
    print("=" * 64)

    # 1. Check dependencies
    ensure_dependencies()

    # 2. Free port 8000 if occupied by previous session
    if is_port_in_use(8000):
        free_port(8000)

    # 3. Determine target port
    target_port = 8000
    if is_port_in_use(target_port):
        target_port = find_available_port(8001)

    url = f"http://localhost:{target_port}"
    print(f"\n[OK] Server Web App:  {url}")
    print(f"[OK] Tai lieu API:     {url}/api/docs")
    print(f"[OK] Dang nhap mau:    Tai khoan: admin  | Mat khau: admin123")
    print("-" * 64)
    print("-> Meo: Trinh duyet web se tu dong mo trong giay lat.")
    print("-> Nhan Ctrl + C de dung Server.")
    print("-" * 64 + "\n")

    # 4. Auto open browser
    def open_browser():
        time.sleep(1.2)
        try:
            webbrowser.open(url)
        except Exception:
            pass

    import threading
    threading.Thread(target=open_browser, daemon=True).start()

    # 5. Run Uvicorn
    import uvicorn
    try:
        uvicorn.run(
            "backend.main:app",
            host="127.0.0.1",
            port=target_port,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n[STOP] Da dung server thanh cong.")
    except Exception as e:
        print(f"\n[LOI] Khong the khoi chay server: {e}")
        input("Nhan Enter de thoat...")

if __name__ == "__main__":
    main()
