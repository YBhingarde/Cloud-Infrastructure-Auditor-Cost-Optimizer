import boto3
import logging
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Any

# Setup basic logging for this module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class EC2MetricsScanner:
    """
    Day 3 Complete: Scanner to identify underutilized EC2 instances 
    based on CloudWatch CPU metrics (< 5% over 14 days).
    """
    
    def __init__(self, region_name: str = 'us-east-1', session: boto3.Session = None):
        """
        Initializes the EC2 and CloudWatch clients.
        """
        self.region = region_name
        try:
            if session:
                self.ec2_client = session.client('ec2', region_name=self.region)
                self.cw_client = session.client('cloudwatch', region_name=self.region)
            else:
                self.ec2_client = boto3.client('ec2', region_name=self.region)
                self.cw_client = boto3.client('cloudwatch', region_name=self.region)
                
            logger.info(f"Successfully initialized AWS clients for region: {self.region}")
        except Exception as e:
            logger.error(f"Failed to initialize AWS clients in {self.region}. Error: {str(e)}")
            raise

    def _get_running_instances(self) -> List[Dict[str, Any]]:
        """
        Fetches all currently RUNNING EC2 instances and extracts metadata.
        """
        running_instances = []
        try:
            logger.info(f"Fetching running EC2 instances in {self.region}...")
            filters = [{'Name': 'instance-state-name', 'Values': ['running']}]
            paginator = self.ec2_client.get_paginator('describe_instances')
            
            for page in paginator.paginate(Filters=filters):
                for reservation in page['Reservations']:
                    for instance in reservation['Instances']:
                        instance_id = instance['InstanceId']
                        tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                        
                        running_instances.append({
                            "instance_id": instance_id,
                            "instance_type": instance['InstanceType'],
                            "tags": tags
                        })
            return running_instances
        except Exception as e:
            logger.error(f"Error fetching EC2 instances: {str(e)}")
            return []

    def _get_average_cpu_utilization(self, instance_id: str) -> float:
        """
        Day 3 Logic: Connects to CloudWatch and calculates the average 
        CPU utilization over a 14-day window.
        """
        try:
            end_time = datetime.now(timezone.utc)
            start_time = end_time - timedelta(days=14)
            
            # Period: 86400 seconds = 1 day interval datapoints
            response = self.cw_client.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=start_time,
                EndTime=end_time,
                Period=86400,
                Statistics=['Average']
            )
            
            datapoints = response.get('Datapoints', [])
            if not datapoints:
                # If no metrics found, assume 0% to alert for low usage
                return 0.0
                
            # Calculate the overall average across all 14 days
            total_cpu = sum(dp['Average'] for dp in datapoints)
            overall_average = total_cpu / len(datapoints)
            
            return round(overall_average, 2)
            
        except Exception as e:
            logger.error(f"Error fetching CloudWatch metrics for {instance_id}: {str(e)}")
            return 0.0

    def get_underutilized_instances(self) -> List[Dict[str, Any]]:
        """
        Main Business Logic: Filters instances that have CPU utilization < 5%.
        Outputs data in the EXACT team dictionary schema contract for Member 4.
        """
        underutilized_resources = []
        running_instances = self._get_running_instances()
        
        logger.info(f"Analyzing CloudWatch metrics for {len(running_instances)} instances...")
        
        for instance in running_instances:
            instance_id = instance['instance_id']
            avg_cpu = self._get_average_cpu_utilization(instance_id)
            
            logger.info(f"Instance {instance_id} has a 14-day Average CPU of: {avg_cpu}%")
            
            # CRITERIA: Check if CPU is strictly less than 5%
            if avg_cpu < 5.0:
                # Match the exact team dictionary contract
                resource_data = {
                    "resource_id": instance_id,
                    "resource_type": "EC2_INSTANCE",
                    "region": self.region,
                    "status": "running",
                    "metrics": {
                        "average_cpu": avg_cpu,
                        "days_window": 14
                    },
                    "tags": instance['tags']
                }
                underutilized_resources.append(resource_data)
                
        logger.info(f"Analysis complete. Identified {len(underutilized_resources)} underutilized instances.")
        return underutilized_resources

# --- Standalone Execution for Testing ---
if __name__ == "__main__":
    # Test in Mumbai region (ap-south-1)
    scanner = EC2MetricsScanner(region_name="ap-south-1")
    results = scanner.get_underutilized_instances()
    
    print("\n--- FINAL OUTPUT CONTRACT FOR MEMBER 4 ---")
    import json
    print(json.dumps(results, indent=4))