from scanners.ebs_scanner import get_unattached_ebs_volumes
from scanners.eip_scanner import get_unassociated_elastic_ips


def get_all_unused_resources():
    resources = []

    resources.extend(get_unattached_ebs_volumes())
    resources.extend(get_unassociated_elastic_ips())

    return resources

if __name__ == "__main__":
    resources = get_all_unused_resources()

    if resources:
        print(f"\nTotal unused resources found: {len(resources)}\n")

        for resource in resources:
            print("-" * 50)
            print(f"Resource Type : {resource['resource_type']}")
            print(f"Region        : {resource['region']}")
            print(f"Resource ID   : {resource['resource_id']}")

            if resource["resource_type"] == "EBS":
                print(f"Size (GB)     : {resource['size']}")

            if resource["resource_type"] == "ElasticIP":
                print(f"Public IP     : {resource['public_ip']}")

            print(f"Status        : {resource['status']}")

    else:
        print("No unused resources found.")