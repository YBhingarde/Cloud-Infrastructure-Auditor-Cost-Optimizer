from aws.auth import authenticate

from aws.session_manager import list_profiles

from aws.regions import SUPPORTED_REGIONS

from utils.logger import log_info


def scan():

    print("\nAvailable Profiles:")

    for i, profile in enumerate(list_profiles(), 1):

        print(f"{i}. {profile}")


    print("\nAvailable Regions:")

    for i, region in enumerate(SUPPORTED_REGIONS, 1):

        print(f"{i}. {region}")


    profile = input("\nEnter AWS Profile: ")

    region = input("Enter AWS Region: ")
    if not profile:
        print("Profile cannot be empty.")
        return
    if not region:
        print("Region cannot be empty.")
        return


    log_info("Scan started")


    if not authenticate(profile, region):

        print("Authentication failed.")

        return


    print("\nScanning resources...")

    print("EC2 Instances : 0")

    print("S3 Buckets : 0")

    print("Lambda Functions : 0")


    log_info("Scan completed")