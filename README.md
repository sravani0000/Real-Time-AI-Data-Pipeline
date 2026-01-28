# AI-Powered Real-Time Tech Sentiment Pipeline

This project is an automated end-to-end data pipeline that fetches live news, performs sentiment analysis using Generative AI, and warehouses the results in the cloud for real-time visualization.


## 🚀 Overview
The pipeline orchestrates a flow between four major platforms to turn unstructured news into actionable insights:
1.  **NewsAPI**: Ingests real-time unstructured headline data.
2.  **Google Gemini 2.0 Flash**: Acts as the "AI Brain" to classify headline sentiment (Positive, Negative, Neutral).
3.  **Google BigQuery**: Stores processed data in a structured, scalable cloud warehouse.
4.  **Looker Studio**: Visualizes industry trends via a dynamic dashboard.

## 🛠️ Technical Stack
* **Language**: Python 3.x
* **AI/ML**: Google Gemini 2.0 Flash (LLM)
* **Cloud Infrastructure**: Google Cloud Platform (GCP)
* **Data Warehouse**: BigQuery
* **BI Tool**: Looker Studio

## 📁 Repository Structure
* `ingestor.py`: The main engine handling API calls, AI classification, and BigQuery Load Jobs.
* `create_table.py`: Infrastructure script to define the BigQuery schema with strict `REQUIRED` modes for data integrity.
* `setup_bq.py`: Script to programmatically initialize the dataset environment.
* `requirements.txt`: Lists all Python dependencies for portability.
* `.gitignore`: Crucial security file to prevent sensitive service account keys and API keys from being exposed.

## 📊 Dashboard Insights
The final dashboard provides a comprehensive look at the tech landscape:
* **Sentiment Ratio**: A pie chart showing the current emotional pulse of tech news (e.g., 40% Positive, 40% Negative, 20% Neutral).
* **Temporal Analysis**: A time-series chart visualizing news volume and sentiment drift over days.
* **Live Feed**: A detailed table displaying the specific headlines processed by the AI.

## 🔧 Setup & Installation
1.  **Clone the Repo**: `git clone https://github.com/your-username/ai-sentiment-pipeline.git`
2.  **Install Dependencies**: `pip install -r requirements.txt`
3.  **Environment Variables**: Create a `.env` file with your `NEWS_API_KEY`, `GEMINI_API_KEY`, and `PROJECT_ID`.
4.  **GCP Authentication**: Place your Service Account JSON key in the root directory.
5.  **Run Infrastructure**: 
    
    python setup_bq.py
    python create_table.py
  
6.  **Execute Pipeline**: 
 
    python ingestor.py
 

---
*Built by Sai Sravani Madabhushi | Data Science & Analytics*
