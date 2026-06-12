import boto3


def get_ec2_client(region_name="us-east-1"):
    """
    Initialize EC2 client for a given AWS region.
    """

    ec2_client = boto3.client(
        "ec2",
        region_name=region_name
    )

    return ec2_client