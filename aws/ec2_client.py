import boto3


def get_ec2_client(region):
    """
    Create an EC2 client for a given AWS region.
    """
    return boto3.client("ec2", region_name=region)