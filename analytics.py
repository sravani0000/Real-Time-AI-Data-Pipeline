import sqlite3

def get_sentiment_summary():
    conn = sqlite3.connect('trends.db')
    cursor = conn.cursor()
    
    # Query to count each sentiment type
    cursor.execute("SELECT sentiment, COUNT(*) FROM tech_trends GROUP BY sentiment")
    results = cursor.fetchall()
    
    print("--- Current Trend Report ---")
    for sentiment, count in results:
        print(f"{sentiment}: {count} articles")
    
    conn.close()

if __name__ == "__main__":
    get_sentiment_summary()