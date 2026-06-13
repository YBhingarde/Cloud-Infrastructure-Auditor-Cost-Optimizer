import boto3
from aws.regions import get_regions


def get_unattached_ebs_volumes():
    unattached_volumes = []

    for region in get_regions():
        ec2 = boto3.client("ec2", region_name=region)

        response = ec2.describe_volumes()

        for volume in response["Volumes"]:
            if volume["State"] == "available":
                unattached_volumes.append(
                    {
                        "Region": region,
                        "VolumeId": volume["VolumeId"],
                        "Size": volume["Size"],
                        "State": volume["State"]
                    }
                )

    return unattached_volumes