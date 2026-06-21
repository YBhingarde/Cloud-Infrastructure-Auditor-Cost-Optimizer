# Handles AWS session creation and profile management

def create_session(profile_name, region):

    return {
        "profile": profile_name,
        "region": region
    }


def list_profiles():

    return [
        "default",
        "dev",
        "prod"
    ]