import boto3
from aws.regions import get_regions
from botocore.exceptions import ClientError
from aws.ec2_client import get_ec2_client


def get_unattached_ebs_volumes():
    unattached_volumes = []

    for region in get_regions():
        ec2 = get_ec2_client(region)

        try:
            response = ec2.describe_volumes()

            for volume in response["Volumes"]:
                if volume["State"] == "available":
                    unattached_volumes.append(
                        {
                            "resource_type": "EBS",
                            "region": region,
                            "resource_id": volume["VolumeId"],
                            "size": volume["Size"],
                            "status": volume["State"],
                        }
                    )

        except ClientError as e:
            print(f"[EBS Scanner] Failed to scan region {region}: {e}")

    return unattached_volumes