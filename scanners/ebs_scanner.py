import boto3

def get_ec2_client(region_name="us-east-1"):
    return boto3.client(
        "ec2",
        region_name=region_name
    )

def get_available_volumes(region_name="us-east-1"):
    ec2_client = get_ec2_client(region_name)

    response = ec2_client.describe_volumes(
        Filters=[
            {
                "Name": "status",
                "Values": ["available"]
            }
        ]
    )

    volume_list = []

    for volume in response["Volumes"]:
        volume_list.append(
            {
                "VolumeId": volume["VolumeId"],
                "Size": volume["Size"],
                "State": volume["State"],
                "Region": region_name
            }
        )

    return volume_list