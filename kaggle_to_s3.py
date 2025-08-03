#!/usr/bin/env python3
"""
Kaggle to S3 Data Pipeline
A standalone script that downloads datasets from Kaggle and uploads them to S3
"""

import os
import sys
import boto3
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Your credentials (already configured in the DAG)
KAGGLE_USERNAME = "mr0nidhi"
KAGGLE_KEY = "cf03d31f447c6031c1a039911310445c"
S3_BUCKET = "kaggle-data-pipeline"  # Change this to your bucket name

def setup_kaggle_credentials():
    """Setup Kaggle API credentials"""
    try:
        # Set environment variables
        os.environ["KAGGLE_USERNAME"] = KAGGLE_USERNAME
        os.environ["KAGGLE_KEY"] = KAGGLE_KEY
        
        # Create kaggle directory if it doesn't exist
        kaggle_dir = os.path.expanduser("~/.kaggle")
        os.makedirs(kaggle_dir, exist_ok=True)
        
        # Create kaggle.json file
        kaggle_json = os.path.join(kaggle_dir, "kaggle.json")
        if not os.path.exists(kaggle_json):
            import json
            credentials = {
                "username": KAGGLE_USERNAME,
                "key": KAGGLE_KEY
            }
            with open(kaggle_json, 'w') as f:
                json.dump(credentials, f)
            os.chmod(kaggle_json, 0o600)
            
        logger.info("Kaggle credentials configured successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to setup Kaggle credentials: {e}")
        return False

def download_tweets_from_kaggle():
    """Download tweets dataset from Kaggle"""
    try:
        api = KaggleApi()
        api.authenticate()
        
        dataset_name = 'mmmarchetti/tweets-dataset'
        download_path = '/tmp/tweets_data'
        os.makedirs(download_path, exist_ok=True)
        
        logger.info(f"Downloading dataset: {dataset_name}")
        api.dataset_download_files(dataset_name, path=download_path, unzip=True)
        
        logger.info("Dataset downloaded successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to download dataset: {e}")
        return False

def upload_to_s3():
    """Upload the downloaded file to S3"""
    try:
        s3 = boto3.client('s3')
        bucket_name = S3_BUCKET
        local_file_path = '/tmp/tweets_data/tweets.csv'
        s3_key = 'kaggle/tweets.csv'
        
        if not os.path.exists(local_file_path):
            logger.error(f"Local file not found: {local_file_path}")
            return False
        
        logger.info(f"Uploading {local_file_path} to s3://{bucket_name}/{s3_key}")
        
        with open(local_file_path, 'rb') as f:
            s3.upload_fileobj(f, bucket_name, s3_key)
        
        logger.info("Upload successful!")
        return True
    except Exception as e:
        logger.error(f"Failed to upload to S3: {e}")
        return False

def main():
    """Main execution function"""
    logger.info("Starting Kaggle to S3 pipeline")
    
    # Step 1: Setup credentials
    if not setup_kaggle_credentials():
        logger.error("Failed to setup credentials. Exiting.")
        sys.exit(1)
    
    # Step 2: Download from Kaggle
    if not download_tweets_from_kaggle():
        logger.error("Failed to download from Kaggle. Exiting.")
        sys.exit(1)
    
    # Step 3: Upload to S3
    if not upload_to_s3():
        logger.error("Failed to upload to S3. Exiting.")
        sys.exit(1)
    
    logger.info("Pipeline completed successfully!")

if __name__ == "__main__":
    main() 