🐦 Fetching Tweets from Kaggle and Uploading to S3 using Airflow
This project demonstrates an end-to-end data pipeline using Apache Airflow that:

Downloads a Tweets Dataset from Kaggle

Processes it (optional)

Uploads the dataset to an Amazon S3 bucket

📁 Project Structure
bash
Copy
Edit
├── dags/
│   └── tweet_pipeline.py         # Airflow DAG
├── .env                          # Environment variables (not committed)
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
⚙️ Technologies Used
Apache Airflow

Python 3

Kaggle API

Amazon S3 (boto3)

AWS EC2 (for hosting Airflow)

VS Code (optional)

🔑 Prerequisites
🐍 Python & Virtual Environment
bash
Copy
Edit
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv airflow_venv
source airflow_venv/bin/activate
🧪 Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
📦 Required Packages (if you don't use requirements.txt)
bash
Copy
Edit
pip install airflow boto3 kaggle pandas
🪪 Kaggle API Setup
Go to: https://www.kaggle.com > Account > Create API Token

This will download a file named kaggle.json

Move it to:

bash
Copy
Edit
mkdir -p ~/.kaggle
mv /path/to/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
OR set environment variables:

bash
Copy
Edit
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_key
🪣 AWS S3 Setup
Create a bucket on S3

Create an IAM user with programmatic access

Save AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY

Configure AWS CLI:

bash
Copy
Edit
aws configure
🛠️ DAG: tweet_pipeline.py
This DAG:

Authenticates with Kaggle

Downloads the dataset

Uploads it to a specified S3 bucket

Example structure inside DAG:

python
Copy
Edit
with DAG(...) as dag:
    fetch_data = PythonOperator(...)
    upload_to_s3 = PythonOperator(...)
    fetch_data >> upload_to_s3
✅ Running the DAG
Launch Airflow UI:

bash
Copy
Edit
airflow db init
airflow webserver --port 8080
airflow scheduler
Open: http://localhost:8080

Enable tweet_pipeline DAG and trigger it.

📤 Output
The final dataset file (e.g., tweets.csv) will be uploaded to:

arduino
Copy
Edit
s3://your-bucket-name/kaggle/tweets.csv
📌 Sample DAG Code Snippet
python
Copy
Edit
def fetch_tweets_from_kaggle():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('your-kaggle-username/tweets-dataset', path='/tmp/', unzip=True)

def upload_to_s3():
    s3 = boto3.client('s3')
    with open('/tmp/tweets.csv', 'rb') as f:
        s3.upload_fileobj(f, 'your-bucket-name', 'tweets.csv')
🏷️ Tags & Hashtags
#airflow #s3 #kaggle #ETL #python #aws #dags #automation #dataengineering
