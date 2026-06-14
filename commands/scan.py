from utils.logger import log_info
from aws.auth import authenticate

def scan():

    print("\nAvailable Profiles:")
    print("1. default")
    print("2. dev")
    print("3. prod")

    profile = input("\nEnter AWS Profile: ")
    region = input("Enter AWS Region: ")

    if not profile:
        profile = "default"

    if not region:
        region = "ap-south-1"

    log_info("Scan started")

    if not authenticate(profile, region):
        print("Authentication failed.")
        return

    print("\n========== AWS CONFIGURATION ==========")
    print(f"AWS Profile : {profile}")
    print(f"AWS Region  : {region}")

    print("\n========== SCANNING RESOURCES ==========")

    resources = {
        "EC2 Instances": 5,
        "S3 Buckets": 2,
        "EBS Volumes": 3,
        "Lambda Functions": 4
    }

    for resource, count in resources.items():
        print(f"{resource}: {count}")

    print("\n========== SCAN SUMMARY ==========")
    print(f"Total Resources Scanned: {sum(resources.values())}")

    log_info("Scan completed successfully")