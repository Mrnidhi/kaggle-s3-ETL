#!/usr/bin/env python3
"""
Test AWS credentials and S3 access
"""

import boto3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_aws_credentials():
    """Test AWS credentials and S3 access"""
    try:
        s3 = boto3.client('s3')
        logger.info("✅ AWS credentials are valid")
        
        bucket_name = "kaggle-data-pipeline"
        try:
            s3.head_bucket(Bucket=bucket_name)
            logger.info(f"✅ S3 bucket '{bucket_name}' is accessible")
            return True
        except Exception as e:
            logger.error(f"❌ Cannot access S3 bucket '{bucket_name}': {e}")
            logger.info("💡 Make sure:")
            logger.info("   1. The bucket exists")
            logger.info("   2. Your AWS credentials have S3 access")
            logger.info("   3. The bucket name is correct")
            return False
            
    except Exception as e:
        logger.error(f"❌ AWS credentials are invalid: {e}")
        logger.info("💡 Please configure AWS credentials using:")
        logger.info("   aws configure")
        return False

if __name__ == "__main__":
    logger.info("Testing AWS credentials and S3 access...")
    test_aws_credentials()
