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
                        "resource_type": "EBS",
                        "region": region,
                        "resource_id": volume["VolumeId"],
                        "size": volume["Size"],
                        "status": volume["State"]
                    }
                )

    return unattached_volumes



if __name__ == "__main__":
    print(get_unattached_ebs_volumes())