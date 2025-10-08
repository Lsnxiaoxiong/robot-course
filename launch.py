import subprocess

from src.app import app

if __name__ == '__main__':
    subprocess.run([
            "gunicorn",
            "--workers", "4",
            "--timeout", "600",
            "--bind", "0.0.0.0:5000",
            "src.app:app"
        ])