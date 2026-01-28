from google.cloud import bigquery
from google.oauth2 import service_account

# 1. Use the same key you just downloaded
KEY_PATH = r"C:\Users\madab\Downloads\cellular-arbor-436405-c0-f8c56f803c50.json"
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)

PROJECT_ID = 'cellular-arbor-436405-c0'
client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

# 2. Define the Table ID
table_id = f"{PROJECT_ID}.tech_sentiment_analysis.live_trends"

# 3. Define the Schema (Columns)
schema = [
    bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("sentiment", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED"),
]

# 4. Create the Table
table = bigquery.Table(table_id, schema=schema)

try:
    table = client.create_table(table)
    print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")
except Exception as e:
    print(f" Notice: {e}")