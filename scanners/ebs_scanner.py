from aws.regions import get_regions
from botocore.exceptions import ClientError
from aws.ec2_client import get_ec2_client


def get_unattached_ebs_volumes():
    """
    Scan all supported regions and return unattached EBS volumes.
    """
    unattached_volumes = []

    for region in get_regions():
        ec2 = get_ec2_client(region)

        try:
            response = ec2.describe_volumes()

            for volume in response["Volumes"]:
                if volume["State"] == "available":
                    unattached_volumes.append(
                        {
                            "resource_type": "EBS",
                            "region": region,
                            "resource_id": volume["VolumeId"],
                            "size": volume["Size"],
                            "status": volume["State"],
                            "estimated_monthly_cost_usd": round(volume["Size"] * 0.10, 2),
                            "metrics": {
                                "average_cpu": "N/A",
                                "days_window": 14,
                                "wasted_cost_usd": 0.0
                            },
                            "tags": {}
                        }
                    )

        except ClientError as e:
            print(f"[EBS Scanner] Failed to scan region {region}: {e}")

    return unattached_volumes


if __name__ == "__main__":
    print(get_unattached_ebs_volumes())