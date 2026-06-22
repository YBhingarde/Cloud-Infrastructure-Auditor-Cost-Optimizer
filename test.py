from scanners.ebs_scanner import get_ec2_client

client = get_ec2_client()

print(client)