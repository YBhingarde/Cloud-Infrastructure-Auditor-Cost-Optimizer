from datetime import datetime

def log_info(message):
    print(f"[INFO] {datetime.now()} - {message}")

def log_error(message):
    print(f"[ERROR] {datetime.now()} - {message}")

def log_warning(message):
    print(f"[WARNING] {datetime.now()} - {message}")