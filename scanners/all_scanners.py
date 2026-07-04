from datetime import datetime

from scanners.ebs_scanner import get_unattached_ebs_volumes
from scanners.eip_scanner import get_unassociated_elastic_ips
from scanners.formatter import format_resource


def get_all_unused_resources():
    """
    Collects unused AWS resources from all available scanner modules.

    Returns:
        list: A list of dictionaries containing information about
        unused EBS volumes and Elastic IPs.
    """
    resources = []

    resources.extend(get_unattached_ebs_volumes())
    resources.extend(get_unassociated_elastic_ips())

    return resources


if __name__ == "__main__":
    resources = get_all_unused_resources()

    scan_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    resources.sort(
        key=lambda resource: resource.get("estimated_monthly_cost_usd", 0),
        reverse=True,
    )

    if resources:
        print("=" * 50)
        print("CLOUD INFRASTRUCTURE AUDITOR")
        print("=" * 50)
        print(f"Scan Time : {scan_time}")
        print()

        print(f"Total unused resources found: {len(resources)}\n")

        total_monthly_waste = 0
        ebs_count = 0
        eip_count = 0

        for resource in resources:
            formatted_resource = format_resource(resource)

            print("=" * 50)

            cost = resource.get("estimated_monthly_cost_usd", 0)

            if cost >= 5:
                print("Priority       : HIGH")
            elif cost >= 2:
                print("Priority       : MEDIUM")
            else:
                print("Priority       : LOW")

            for key, value in formatted_resource.items():
                print(f"{key:<15}: {value}")

            if resource["resource_type"] == "EBS":
                ebs_count += 1
                print(f"Size (GB)      : {resource['size']}")
                recommendation = "Delete unattached EBS volume if no longer needed."

            elif resource["resource_type"] == "ElasticIP":
                eip_count += 1
                print(f"Public IP      : {resource['public_ip']}")
                recommendation = "Release unused Elastic IP to avoid charges."

            else:
                recommendation = "Review this resource."

            print(f"Estimated Cost : ${cost:.2f}/month")
            print(f"Recommendation : {recommendation}")

            total_monthly_waste += cost

        print("\n" + "=" * 50)
        print("SCAN SUMMARY")
        print("=" * 50)
        print(f"EBS Volumes Found     : {ebs_count}")
        print(f"Elastic IPs Found     : {eip_count}")
        print(f"Total Resources Found : {len(resources)}")
        print(f"Monthly Waste         : ${total_monthly_waste:.2f}")
        print(f"Potential Savings     : ${total_monthly_waste:.2f}/month")
        print("Suggested Action      : Clean up unused resources to reduce AWS costs.")
        print("=" * 50)

        print("\nScan Status           : COMPLETED")
        print("Audit Result          : SUCCESS")
        print(f"Report Generated At   : {scan_time}")

    else:
        print("=" * 50)
        print("CLOUD INFRASTRUCTURE AUDITOR")
        print("=" * 50)
        print(f"Scan Time : {scan_time}")
        print("\nNo unused resources found.")
        print("Scan Status           : COMPLETED")