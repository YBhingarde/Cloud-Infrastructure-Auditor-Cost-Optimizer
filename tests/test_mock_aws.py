from moto import mock_s3
import boto3

@mock_s3
def test_create_bucket():
    s3 = boto3.client("s3", region_name="us-east-1")

    s3.create_bucket(Bucket="test-bucket")

    buckets = s3.list_buckets()

    assert len(buckets["Buckets"]) == 1
    assert buckets["Buckets"][0]["Name"] == "test-bucket"