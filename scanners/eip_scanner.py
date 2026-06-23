from aws.regions import get_regions
from botocore.exceptions import ClientError
from aws.ec2_client import get_ec2_client


def get_unassociated_elastic_ips():
    """
    Scan all supported regions and return unassociated Elastic IPs.
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
                            "metrics": {
                                "average_cpu": "N/A",
                                "days_window": 14,
                                "wasted_cost_usd": 0.0
                            },
                            "tags": {}
                        }
                    )

        except ClientError as e:
            print(f"[EIP Scanner] Failed to scan region {region}: {e}")

    return unused_ips


if __name__ == "__main__":
    print(get_unassociated_elastic_ips())
