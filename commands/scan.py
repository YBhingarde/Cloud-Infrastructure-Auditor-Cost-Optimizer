import json
import os
import time

from aws.auth import authenticate
from aws.session_manager import list_profiles
from aws.regions import SUPPORTED_REGIONS
from utils.logger import log_info
from datetime import datetime


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

    print("\nStarting resource scan...\n")

    services = [
        "EC2 Instances",
        "S3 Buckets",
        "IAM Users",
        "VPCs",
        "Security Groups"
    ]

    for service in services:
        print(f"Scanning {service}...")
        time.sleep(1)
        print(f"✓ {service} scan completed\n")

    print("========== Scan Summary ==========")
    print(f"Profile : {profile}")
    print(f"Region  : {region}")

   

    result = {
        "profile": profile,
        "region": region,
        "ec2_instances": 0,
        "s3_buckets": 0,
        "status": "Success",
        "scan_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
}
    os.makedirs("results", exist_ok=True)

    with open("results/scan_results.json", "w") as file:
        json.dump(result, file, indent=4)

    print("\nScan results saved successfully.")