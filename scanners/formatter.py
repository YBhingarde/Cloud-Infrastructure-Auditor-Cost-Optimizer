def format_resource(resource):
    return {
        "Resource Type": resource["resource_type"],
        "Region": resource["region"],
        "Resource ID": resource["resource_id"],
        "Status": resource["status"]
    }