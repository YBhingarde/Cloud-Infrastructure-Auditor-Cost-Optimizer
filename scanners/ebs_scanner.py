import boto3

# Create EC2 client
ec2 = boto3.client("ec2", region_name="us-east-1")

# Get all EBS volumes
response = ec2.describe_volumes()

# Print all volume information
print(response)