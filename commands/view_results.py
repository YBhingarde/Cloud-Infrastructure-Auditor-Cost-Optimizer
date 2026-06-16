import json

def view_results():

    try:

        with open("results.json", "r") as file:

            data = json.load(file)

        print("\n===== Scan Results =====")

        print(f"AWS Profile : {data['profile']}")

        print(f"AWS Region : {data['region']}")

        print(f"EC2 Instances : {data['ec2']}")

        print(f"S3 Buckets : {data['s3']}")

    except:

        print("No scan results found. Run option 1 first.")