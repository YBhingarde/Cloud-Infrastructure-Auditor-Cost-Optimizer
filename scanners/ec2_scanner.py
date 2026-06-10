import boto3
import logging
from typing import List, Dict, Any

# Setup basic logging for this module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class EC2MetricsScanner:
    """
    Scanner to identify underutilized EC2 instances based on CloudWatch CPU metrics.
    """
    
    def __init__(self, region_name: str = 'us-east-1', session: boto3.Session = None):
        """
        Day 1: Connect to EC2 and CloudWatch clients safely.
        Accepts an optional Boto3 session from Member 1's config, otherwise defaults to standard boto3.
        """
        self.region = region_name
        
        try:
            if session:
                self.ec2_client = session.client('ec2', region_name=self.region)
                self.cw_client = session.client('cloudwatch', region_name=self.region)
            else:
                # Fallback for standalone testing before Member 1 finishes their module
                self.ec2_client = boto3.client('ec2', region_name=self.region)
                self.cw_client = boto3.client('cloudwatch', region_name=self.region)
                
            logger.info(f"Successfully initialized EC2 & CloudWatch clients for region: {self.region}")
            
        except Exception as e:
            logger.error(f"Failed to initialize AWS clients in {self.region}. Error: {str(e)}")
            raise

    def get_underutilized_instances(self) -> List[Dict[str, Any]]:
        """
        Main execution function. 
        Days 2 & 3 logic (Fetching instances and CloudWatch Math) will be built here.
        """
        underutilized_instances = []
        
        # TODO: Day 2 - Loop through instances data
        # TODO: Day 3 - CPU utilization average calculations logic
        
        return underutilized_instances

# --- Standalone Execution block for Day 1 Testing ---
if __name__ == "__main__":
    # Test your client initialization
    scanner = EC2MetricsScanner(region_name="ap-south-1") # Testing in Mumbai region
    print("Day 1 Setup Complete. Ready for Day 2 logic.")