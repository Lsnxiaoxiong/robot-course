import subprocess

from src.app import app

if __name__ == '__main__':
    subprocess.run([
        "gunicorn",
        "--workers", "1",
        "--threads", "4",
        "--timeout", "600",
        "--bind", "0.0.0.0:50000",
        "src.app:app"
    ])
