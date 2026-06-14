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
                        "AllocationId": address.get("AllocationId"),
                    }
                )

    return unused_ips


if __name__ == "__main__":
    unused_ips = get_unassociated_elastic_ips()

    if unused_ips:
        print("Unused Elastic IPs:")
        for ip in unused_ips:
            print(ip)
    else:
        print("No unused Elastic IPs found.")