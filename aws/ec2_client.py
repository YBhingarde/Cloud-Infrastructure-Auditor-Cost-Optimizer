import boto3


def get_ec2_client(region):
    return boto3.client("ec2", region_name=region)