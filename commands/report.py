import json

def generate_report():

    try:

        with open("results.json", "r") as file:

            data = json.load(file)

        with open("report.txt", "w") as report:

            report.write("Cloud Infrastructure Report\n")

            report.write("---------------------------\n")

            report.write(f"Profile : {data['profile']}\n")

            report.write(f"Region : {data['region']}\n")

            report.write(f"EC2 : {data['ec2']}\n")

            report.write(f"S3 : {data['s3']}\n")

        print("Report generated successfully.")

    except:

        print("No scan results available.")