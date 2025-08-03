# Kaggle to S3 Data Pipeline

I built this project to automatically download Twitter datasets from Kaggle and upload them to Amazon S3. This helps me collect and store social media data for analysis.

## What This Project Does

This pipeline does three main things:
1. Downloads Twitter data from Kaggle
2. Saves it to my computer temporarily
3. Uploads it to Amazon S3 for safe storage

## How I Built It

I used Python to create this project. Here's what I learned and used:

- **Python**: Main programming language
- **Kaggle API**: To download datasets
- **AWS S3**: To store data in the cloud
- **boto3**: Python library for AWS services

## Project Files

```
kaggle_to_s3/
├── kaggle_to_s3.py          # Main script that runs everything
├── test_aws.py              # Tests if AWS is working
├── requirements.txt         # Lists all Python packages needed
├── README.md               # This file
├── SETUP.md                # How to set up the project
└── .gitignore              # Tells Git what files to ignore
```

## How to Use

### Step 1: Install Python Packages
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Credentials
You need to add your Kaggle and AWS credentials in the `kaggle_to_s3.py` file.

### Step 3: Run the Pipeline
```bash
python kaggle_to_s3.py
```

## What Data I'm Working With

The pipeline downloads a Twitter dataset that contains:
- 58,000+ tweets
- Information like username, tweet text, date, likes, shares
- Data is about 7.8 MB in size

## Challenges I Faced

1. **AWS Permissions**: I had to learn about AWS IAM and S3 permissions
2. **API Authentication**: Setting up Kaggle API keys was tricky
3. **Error Handling**: Making sure the script doesn't crash if something goes wrong
4. **Data Processing**: Learning how to work with large CSV files

## What I Learned

- How to use APIs to download data
- How to work with cloud storage (AWS S3)
- How to handle errors in Python
- How to structure a data pipeline project
- How to use Git for version control

## Future Improvements

I want to add these features later:
- Schedule the pipeline to run automatically
- Add more data processing steps
- Support different types of datasets
- Add email notifications when the job is done

## Setup Instructions

See the `SETUP.md` file for detailed setup instructions.

## Testing

To test if everything is working:
```bash
python test_aws.py
```

This will check if your AWS credentials are set up correctly.

---

*This project was built as part of my data engineering learning journey.*
