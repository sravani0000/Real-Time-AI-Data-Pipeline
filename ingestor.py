import requests
import time
from google import genai
from google.cloud import bigquery
from google.oauth2 import service_account

from setup_bq import PROJECT_ID

# --- CONFIGURATION ---
KEY_PATH = r"C:\Users\madab\Downloads\cellular-arbor-436405-c0-f8c56f803c50.json"

# Initialize Clients
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
bq_client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
ai_client = genai.Client(api_key=GEMINI_API_KEY)

def get_tech_news():
    url = f'https://newsapi.org/v2/top-headlines?category=general&language=en&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    return response.json().get('articles', []) if response.status_code == 200 else []

def analyze_sentiment(headline):
    prompt = f"Analyze sentiment: '{headline}'. Reply with ONLY: Positive, Negative, or Neutral."
    response = ai_client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text.strip()

def save_to_bigquery(title, sentiment):
    table_id = f"{PROJECT_ID}.tech_sentiment_analysis.live_trends"
    
    rows_to_insert = [
        {
            "title": title, 
            "sentiment": sentiment, 
            "timestamp": str(time.strftime('%Y-%m-%d %H:%M:%S'))
        }
    ]
    
    # We MUST specify 'mode="REQUIRED"' to match your existing table
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("title", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("sentiment", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED"),
        ],
        write_disposition="WRITE_APPEND",
    )

    load_job = bq_client.load_table_from_json(
        rows_to_insert, 
        table_id, 
        job_config=job_config
    )
    
    load_job.result() # Wait for completion
    print(" Load Job Finished.  Data is now in the Cloud.")

def main():
    print(" AI Trend Engine: Cloud Edition ")
    articles = get_tech_news()
    
    for art in articles[:5]:
        title = art['title']
        try:
            sentiment = analyze_sentiment(title)
            print(f"[{sentiment}] {title[:60]}...")
            save_to_bigquery(title, sentiment)
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(4)

if __name__ == "__main__":
    main()