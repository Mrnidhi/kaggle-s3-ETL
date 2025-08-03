# KaggleS3Pipeline Setup Guide

## 🎉 **Great News!**
Your project is almost ready! The Kaggle download is working perfectly. Here's what's left to complete:

## ✅ **What's Already Working:**
- ✅ Python virtual environment created
- ✅ All dependencies installed
- ✅ Kaggle credentials configured
- ✅ Kaggle dataset download working
- ✅ Standalone script created

## 🔧 **Remaining Setup:**

### **1. Configure AWS Credentials**
You need to set up AWS credentials for S3 access. Choose one method:

#### **Option A: AWS CLI Configuration (Recommended)**
```bash
# Configure AWS credentials
aws configure

# You'll be prompted for:
# - AWS Access Key ID: [Enter your access key]
# - AWS Secret Access Key: [Enter your secret key]
# - Default region: us-east-1 (or your preferred region)
# - Default output format: json
```

#### **Option B: Environment Variables**
```bash
# Set environment variables
export AWS_ACCESS_KEY_ID=your_access_key_here
export AWS_SECRET_ACCESS_KEY=your_secret_key_here
export AWS_DEFAULT_REGION=us-east-1
```

#### **Option C: AWS Credentials File**
```bash
# Create credentials file
mkdir -p ~/.aws
nano ~/.aws/credentials

# Add your credentials:
[default]
aws_access_key_id = your_access_key_here
aws_secret_access_key = your_secret_key_here
```

### **2. Get AWS Credentials**
To get your AWS credentials:
1. Go to [AWS Console](https://aws.amazon.com/console/)
2. Navigate to IAM → Users → Your User
3. Go to "Security credentials" tab
4. Create access keys
5. Save the Access Key ID and Secret Access Key

### **3. Test the Pipeline**
Once AWS credentials are configured:
```bash
# Activate virtual environment
source airflow_venv/bin/activate

# Run the pipeline
python kaggle_to_s3.py
```

## 🚀 **Expected Output:**
```
2025-08-03 02:37:08,061 - INFO - Starting Kaggle to S3 pipeline
2025-08-03 02:37:08,061 - INFO - Kaggle credentials configured successfully
2025-08-03 02:37:08,064 - INFO - Downloading dataset: mmmarchetti/tweets-dataset
2025-08-03 02:37:08,956 - INFO - Dataset downloaded successfully
2025-08-03 02:37:09,044 - INFO - Uploading /tmp/tweets_data/tweets.csv to s3://airflow-ec2-s3/kaggle/tweets.csv
2025-08-03 02:37:09,055 - INFO - Upload successful!
2025-08-03 02:37:09,055 - INFO - Pipeline completed successfully!
```

## 📁 **Project Structure:**
```
kaggle_to_s3/
├── kaggle_to_s3.py          # Main pipeline script
├── dag/twitter_dag.py       # Airflow DAG (for reference)
├── requirements.txt         # Python dependencies
├── airflow_venv/           # Virtual environment
├── README.md               # Project documentation
└── SETUP.md               # This setup guide
```

## 🔍 **What the Pipeline Does:**
1. **Downloads** tweets dataset from Kaggle (`mmmarchetti/tweets-dataset`)
2. **Saves** to local directory (`/tmp/tweets_data/`)
3. **Uploads** to your S3 bucket (`airflow-ec2-s3/kaggle/tweets.csv`)

## 🎯 **Next Steps:**
1. Configure AWS credentials using one of the methods above
2. Run `python kaggle_to_s3.py`
3. Check your S3 bucket for the uploaded file
4. Celebrate! 🎉

## 💡 **Optional: Schedule the Pipeline**
You can schedule this script to run automatically using:
- **Cron jobs** (Linux/Mac)
- **Task Scheduler** (Windows)
- **Cloud services** (AWS Lambda, Google Cloud Functions)

## 🆘 **Need Help?**
If you encounter any issues:
1. Check that AWS credentials are properly configured
2. Verify your S3 bucket exists and is accessible
3. Ensure you have the necessary AWS permissions (S3:PutObject) 