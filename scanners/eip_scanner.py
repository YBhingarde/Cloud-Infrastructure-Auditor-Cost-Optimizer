from aws.regions import get_regions
from botocore.exceptions import ClientError
from aws.ec2_client import get_ec2_client


def get_unassociated_elastic_ips():
    """
    Scans all supported AWS regions and identifies
    unassociated Elastic IP addresses.

    Returns:
        list: List of unused Elastic IP details.
    """
    unused_ips = []

    for region in get_regions():
        ec2 = get_ec2_client(region)

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
                            "status": "unassociated",
                            "estimated_monthly_cost_usd": 3.60,
                        }
                    )

        except ClientError as e:
            print(f"[EIP Scanner] Failed to scan region {region}: {e}")

    return unused_ips
