# 🐦 KaggleS3Pipeline

A Python data pipeline that automatically downloads Twitter datasets from Kaggle and uploads them to Amazon S3.

## 🚀 Features

- **Automated Data Collection**: Downloads Twitter datasets from Kaggle
- **Cloud Storage**: Uploads data to Amazon S3 for secure storage
- **Error Handling**: Robust error handling and logging
- **Easy Setup**: Simple configuration and deployment

## 📁 Project Structure

```
kaggle_to_s3/
├── kaggle_to_s3.py          # Main pipeline script
├── test_aws.py              # AWS credentials tester
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── SETUP.md                # Setup guide
└── .gitignore              # Git ignore rules
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- AWS Account with S3 access
- Kaggle Account with API access

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd kaggle_to_s3
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure credentials**
   - Set up Kaggle API credentials
   - Configure AWS credentials using `aws configure`

## 🔧 Configuration

### Kaggle Credentials
Update the credentials in `kaggle_to_s3.py`:
```python
KAGGLE_USERNAME = "your_kaggle_username"
KAGGLE_KEY = "your_kaggle_key"
```

### S3 Configuration
Update the S3 bucket name in `kaggle_to_s3.py`:
```python
S3_BUCKET = "your-s3-bucket-name"
```

## 🚀 Usage

### Run the Pipeline
```bash
python kaggle_to_s3.py
```

### Test AWS Credentials
```bash
python test_aws.py
```

## 📊 Data Flow

```
Kaggle Dataset → Local Processing → Amazon S3
     ↓              ↓              ↓
  Download      Extract/Store    Cloud Upload
```

### Current Dataset
- **Source**: `mmmarchetti/tweets-dataset` on Kaggle
- **Content**: Twitter posts with metadata
- **Size**: ~7.8MB (58,000+ tweets)
- **Format**: CSV

## 🔍 Monitoring

### Check Local Files
```bash
ls -la /tmp/tweets_data/
head -5 /tmp/tweets_data/tweets.csv
```

### Check S3 Upload
```bash
aws s3 ls s3://your-bucket-name/kaggle/
```

## 🛡️ Security

- Credentials are stored securely
- S3 bucket permissions are configurable
- No sensitive data is committed to Git

## 📈 Future Enhancements

- [ ] Schedule automatic runs
- [ ] Add data processing steps
- [ ] Support multiple datasets
- [ ] Add monitoring and alerts
- [ ] Deploy to cloud services

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:
1. Check the [SETUP.md](SETUP.md) guide
2. Review the error logs
3. Open an issue on GitHub

---

**Built with ❤️ for data engineering**
