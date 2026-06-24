from scanners.ebs_scanner import get_unattached_ebs_volumes
from scanners.eip_scanner import get_unassociated_elastic_ips
from scanners.formatter import format_resource


def get_all_unused_resources():
    """
    Combine results from all scanners.
    """
    resources = []

    resources.extend(get_unattached_ebs_volumes())
    resources.extend(get_unassociated_elastic_ips())

    return resources


if __name__ == "__main__":
    resources = get_all_unused_resources()

    if resources:
        print(f"\nTotal unused resources found: {len(resources)}\n")

        total_monthly_waste = 0

        for resource in resources:
            formatted_resource = format_resource(resource)

            print("-" * 50)

            for key, value in formatted_resource.items():
                print(f"{key:<15}: {value}")

            if resource["resource_type"] == "EBS":
                print(f"Size (GB)      : {resource['size']}")

            if resource["resource_type"] == "ElasticIP":
                print(f"Public IP      : {resource['public_ip']}")

            if "estimated_monthly_cost_usd" in resource:
                print(
                    f"Estimated Cost : ${resource['estimated_monthly_cost_usd']}/month"
                )

                total_monthly_waste += resource["estimated_monthly_cost_usd"]

        print("\n" + "=" * 50)
        print(
            f"TOTAL ESTIMATED MONTHLY WASTE: ${total_monthly_waste:.2f}"
        )
        print("=" * 50)

    else:
        print("No unused resources found.")