import boto3
from aws.regions import get_regions
from botocore.exceptions import ClientError


def get_unassociated_elastic_ips():
    unused_ips = []

    for region in get_regions():
        ec2 = boto3.client("ec2", region_name=region)

        try:
            response = ec2.describe_addresses()

            for address in response["Addresses"]:
                if "AssociationId" not in address:
                    unused_ips.append(
                        {
                            "resource_type": "ElasticIP",
                            "region": region,
                            "resource_id": address.get("AllocationId"),
                            "public_ip": address["PublicIp"],
                            "status": "unassociated"
                        }
                    )

        except ClientError as e:
            print(f"[EIP Scanner] Failed to scan region {region}: {e}") 

    return unused_ips


