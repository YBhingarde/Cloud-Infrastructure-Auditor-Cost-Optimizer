from aws.session_manager import create_session
from utils.logger import log_info, log_error

def authenticate(profile, region):

    session = create_session(profile, region)

    if not session:
        log_error("Unable to create AWS session")
        return False

    log_info(f"AWS Profile: {session['profile']}")
    log_info(f"AWS Region: {session['region']}")
    log_info("AWS credentials validated")

    return True