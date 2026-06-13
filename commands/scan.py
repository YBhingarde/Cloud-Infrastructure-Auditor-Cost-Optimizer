from config.settings import load_settings
from utils.logger import log_info
from aws.auth import authenticate

def scan():
    settings = load_settings()

    log_info("Scan started")

    authenticate()

    print(f"AWS Profile: {settings['aws_profile']}")
    print(f"AWS Region: {settings['aws_region']}")
    print("Scanning cloud resources...")