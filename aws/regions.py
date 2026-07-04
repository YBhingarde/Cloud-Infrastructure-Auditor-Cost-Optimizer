SUPPORTED_REGIONS = [

    "ap-south-1",

    "us-east-1",

    "us-west-2"
]


def validate_region(region):

    return region in SUPPORTED_REGIONS