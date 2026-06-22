def format_resource(resource):
    """
    Format resource information for reporting.
    """
    return {
        "Resource Type": resource["resource_type"],
        "Region": resource["region"],
        "Resource ID": resource["resource_id"],
        "Status": resource["status"]
    }