from google.cloud import bigquery
from google.oauth2 import service_account

# 1. Path to your downloaded JSON key
KEY_PATH = r"C:\Users\madab\Downloads\cellular-arbor-436405-c0-f8c56f803c50.json"

# 2. Create credentials from the file
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)

# 3. Initialize the client with those credentials
PROJECT_ID = 'cellular-arbor-436405-c0'
client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

# 4. Create the Dataset
dataset_id = f"{PROJECT_ID}.tech_sentiment_analysis"
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US" 

try:
    dataset = client.create_dataset(dataset, timeout=30)
    print(f"  Created dataset {dataset_id}")
except Exception as e:
    print(f" Notice: {e}")