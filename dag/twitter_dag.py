from airflow import DAG
import os
from airflow.operators.python import PythonOperator
from datetime import datetime
os.environ["KAGGLE_USERNAME"]="nikhileshwar316" #put your kaggle user_name and kaggle key
os.environ["KAGGLE_KEY"]="4a5530f15f320b5cea17545ad0d3bcf3"
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import boto3

def download_tweets_from_kaggle():
    api = KaggleApi()
    api.authenticate()

    dataset_name = 'mmmarchetti/tweets-dataset' # dataset provided username along with datset name
    download_path = '/tmp/tweets_data'
    os.makedirs(download_path, exist_ok=True)

    api.dataset_download_files(dataset_name, path=download_path, unzip=True)

def upload_to_s3():
    s3 = boto3.client('s3')
    bucket_name = 'airflow-ec2-s3'  # place your S3 bucket
    local_file_path = '/tmp/tweets_data/tweets.csv'  # file path in local
    s3_key = 'kaggle/tweets.csv'  # Path inside S3

    with open(local_file_path, 'rb') as f:
        s3.upload_fileobj(f, bucket_name, s3_key)
    print("Upload successful!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 7, 25),
    'retries': 1,
}

with DAG(
    dag_id='kaggle_to_s3_tweets',
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=['kaggle', 's3', 'tweets']
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_tweets_from_kaggle',
        python_callable=download_tweets_from_kaggle
    )

    upload_task = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3
    )

    fetch_task >> upload_task
