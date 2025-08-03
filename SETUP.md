# How to Set Up This Project

This guide will help you set up the Kaggle to S3 pipeline on your computer.

## What You Need

Before starting, make sure you have:
- Python 3.8 or higher installed
- A Kaggle account
- An AWS account

## Step 1: Download the Project

First, download this project to your computer:
```bash
git clone https://github.com/Mrnidhi/kaggle-s3-ETL.git
cd kaggle-s3-ETL
```

## Step 2: Install Python Packages

Create a virtual environment and install the required packages:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 3: Get Kaggle Credentials

1. Go to [Kaggle](https://www.kaggle.com) and sign in
2. Click on your profile picture → Account
3. Scroll down to "API" section
4. Click "Create New API Token"
5. Download the kaggle.json file
6. Open the file and copy your username and key

## Step 4: Update the Script

Open `kaggle_to_s3.py` and change these lines:
```python
KAGGLE_USERNAME = "your_kaggle_username"
KAGGLE_KEY = "your_kaggle_key"
S3_BUCKET = "your_s3_bucket_name"
```

## Step 5: Set Up AWS

1. Go to [AWS Console](https://aws.amazon.com/console/)
2. Create an S3 bucket or use an existing one
3. Get your AWS access keys:
   - Go to IAM → Users → Your User
   - Security credentials → Create access key
4. Configure AWS on your computer:
```bash
aws configure
```

## Step 6: Test Everything

Test if AWS is working:
```bash
python test_aws.py
```

## Step 7: Run the Pipeline

Now you can run the main script:
```bash
python kaggle_to_s3.py
```

## What Should Happen

When you run the script, you should see messages like:
```
2025-08-03 02:50:44 - INFO - Starting Kaggle to S3 pipeline
2025-08-03 02:50:44 - INFO - Kaggle credentials configured successfully
2025-08-03 02:50:44 - INFO - Downloading dataset: mmmarchetti/tweets-dataset
2025-08-03 02:50:45 - INFO - Dataset downloaded successfully
2025-08-03 02:50:45 - INFO - Uploading /tmp/tweets_data/tweets.csv to s3://your-bucket/kaggle/tweets.csv
2025-08-03 02:50:46 - INFO - Upload successful!
2025-08-03 02:50:46 - INFO - Pipeline completed successfully!
```

## Troubleshooting

### If AWS doesn't work:
- Make sure you ran `aws configure`
- Check if your S3 bucket exists
- Verify your AWS permissions

### If Kaggle doesn't work:
- Check your username and key in the script
- Make sure your Kaggle account is active

### If Python packages fail to install:
- Make sure you're using Python 3.8 or higher
- Try updating pip: `pip install --upgrade pip`

## Need Help?

If you get stuck, check:
1. All credentials are correct
2. You have internet connection
3. Your AWS and Kaggle accounts are active

---

*This setup guide was written to help others use this project easily.*
