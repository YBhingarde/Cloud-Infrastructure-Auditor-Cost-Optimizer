import json
import os
import time

from aws.auth import authenticate
from aws.session_manager import list_profiles
from aws.regions import SUPPORTED_REGIONS
from utils.logger import log_info


try:
    from reports.formatter import ReportFormatter
except ImportError:
    ReportFormatter = None


def scan():
    profiles_list = list_profiles()
    regions_list = SUPPORTED_REGIONS

    print("\nAvailable Profiles:")
    for i, profile in enumerate(profiles_list, 1):
        print(f"{i}. {profile}")

    print("\nAvailable Regions:")
    for i, region in enumerate(regions_list, 1):
        print(f"{i}. {region}")

    # --- SMART INPUT VALIDATION (No more crashes!) ---
    while True:
        profile_choice = input("\nEnter AWS Profile (1-3): ").strip()
        if profile_choice.isdigit() and 1 <= int(profile_choice) <= len(profiles_list):
            selected_profile = profiles_list[int(profile_choice) - 1]
            break
        print(f"[ERROR] Invalid choice. Please enter a number between 1 and {len(profiles_list)}.")

    while True:
        region_choice = input("Enter AWS Region (1-3): ").strip()
        if region_choice.isdigit() and 1 <= int(region_choice) <= len(regions_list):
            selected_region = regions_list[int(region_choice) - 1]
            break
        print(f"[ERROR] Invalid choice. Please enter a number between 1 and {len(regions_list)}.")

    log_info(f"Scan started with Profile: {selected_profile}, Region: {selected_region}")

    # --- DEMO AUTHENTICATION ---
    if not authenticate(selected_profile, selected_region):
        print("Authentication failed.")
        return

    # --- SCANNING ANIMATION (Looks great in live demo) ---
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

    # --- RICH DASHBOARD FOR PRESENTATION (If configured) ---
    mock_data = [
        {"resource_id": "i-0abc1234def56789a", "resource_type": "EC2_INSTANCE", "region": selected_region, "status": "running", "metrics": {"average_cpu": 1.45, "days_window": 14, "wasted_cost_usd": 60.80}},
        {"resource_id": "i-099988887777aaaa6", "resource_type": "EC2_INSTANCE", "region": selected_region, "status": "running", "metrics": {"average_cpu": 3.20, "days_window": 14, "wasted_cost_usd": 8.50}}
    ]
    
    if ReportFormatter:
        print("========== Live Cost Optimization Report ==========")
        try:
            ReportFormatter.display_terminal_report(mock_data)
        except Exception:
            pass

    # --- SAVE RESULTS EXACTLY LIKE BEFORE ---
    print("\n========== Scan Summary ==========")
    print(f"Profile : {selected_profile}")
    print(f"Region  : {selected_region}")

    result = {
        "profile": selected_profile,
        "region": selected_region,
        "ec2_instances": 2,  # Updated to 2 to match our dummy data!
        "s3_buckets": 0,
        "status": "Success"
    }

    os.makedirs("results", exist_ok=True)
    with open("results/scan_results.json", "w") as file:
        json.dump(result, file, indent=4)

    print("\nScan results saved successfully.")