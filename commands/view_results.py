import json
import os

def view_results():

    file_path = "results/scan_results.json"

    if not os.path.exists(file_path):
        print("\nNo scan results found.")
        return

    with open(file_path, "r") as file:
        result = json.load(file)

    print("\n========== Previous Scan ==========")
    print(f"Profile : {result['profile']}")
    print(f"Region  : {result['region']}")
    print(f"EC2 Instances : {result['ec2_instances']}")
    print(f"S3 Buckets    : {result['s3_buckets']}")
    print(f"Status        : {result['status']}")
    print("===================================")
    print(f"Scan Time     : {result['scan_time']}")