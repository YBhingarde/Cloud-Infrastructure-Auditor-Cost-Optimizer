import boto3
from aws.regions import get_regions


def get_unassociated_elastic_ips():
    unused_ips = []

    for region in get_regions():
        ec2 = boto3.client("ec2", region_name=region)

        response = ec2.describe_addresses()

        for address in response["Addresses"]:
            if "AssociationId" not in address:
                unused_ips.append(
                    {
                        "Region": region,
                        "PublicIp": address["PublicIp"],
                        "AllocationId": address.get("AllocationId")
                    }
                )

    return unused_ips