from scanners.ebs_scanner import get_unattached_ebs_volumes
from scanners.eip_scanner import get_unassociated_elastic_ips


def get_all_unused_resources():
    resources = []

    resources.extend(get_unattached_ebs_volumes())
    resources.extend(get_unassociated_elastic_ips())

    return resources


if __name__ == "__main__":
    print(get_all_unused_resources())