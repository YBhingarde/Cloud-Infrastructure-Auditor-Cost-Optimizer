import json
import os

def generate_report():
    file_path = "results/scan_results.json"

    if not os.path.exists(file_path):
        print("\nNo scan results found. Run Scan Resources first.")
        return

    with open(file_path, "r") as file:
        result = json.load(file)

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/report.txt"

    with open(report_path, "w") as report:
        report.write("Cloud Infrastructure Audit Report\n")
        report.write("=" * 40 + "\n")
        report.write(f"Profile : {result['profile']}\n")
        report.write(f"Region  : {result['region']}\n")
        report.write(f"EC2 Instances : {result['ec2_instances']}\n")
        report.write(f"S3 Buckets    : {result['s3_buckets']}\n")
        report.write(f"Status        : {result['status']}\n")

    print(f"\nReport generated successfully!")
    print(f"Saved to: {report_path}")