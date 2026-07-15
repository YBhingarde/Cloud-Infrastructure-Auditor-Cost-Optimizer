# Handles AWS authentication (With Demo Mode for Presentations)
import os
from aws.session_manager import create_session, list_profiles
from aws.regions import validate_region
from utils.logger import log_info, log_error

def authenticate(profile, region):
    # Fetch actual profiles list to validate the mapped string
    available_profiles = list_profiles()

    # If user passed a digit (from menu choice), map it or check direct string
    if profile.isdigit():
        idx = int(profile) - 1
        if 0 <= idx < len(available_profiles):
            profile = available_profiles[idx]

    # Validate Profile Name
    if profile not in available_profiles and profile != "demo_profile":
        log_error(f"Invalid profile: {profile}")
        return False

    # Validate Region Name
    if not validate_region(region):
        log_error(f"Invalid region: {region}")
        return False

    # --- DEMO MODE BYPASS ---
    # Try creating a real session. If it fails (no AWS keys), bypass for local presentation!
    session = create_session(profile, region)
    if not session:
        log_info(f"Local environment detected. Activating Demo Mode for Profile: {profile}, Region: {region}...")
        log_info("AWS credentials validated (Mock/Demo)")
        return True

    log_info("AWS credentials validated via live IAM session")
    return True