from aws.session_manager import create_session, list_profiles

from aws.regions import validate_region

from utils.logger import log_info, log_error


def authenticate(profile, region):

    if profile not in list_profiles():

        log_error("Invalid profile")

        return False


    if not validate_region(region):

        log_error("Invalid region")

        return False


    session = create_session(profile, region)

    if not session:

        log_error("Authentication failed")

        return False


    log_info("AWS credentials validated")

    return True