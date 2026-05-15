import pandas as pd
import spacy
from transformers import pipeline
import os

# Load resources
print("Loading Transformer model and spaCy...")
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
nlp = spacy.load("en_core_web_sm")

def get_theme(text):
    """Simple keyword-based thematic grouping"""
    text = text.lower()
    if any(word in text for word in ['login', 'password', 'access', 'account', 'sign in']):
        return "Account Access"
    if any(word in text for word in ['transfer', 'slow', 'wait', 'transaction', 'failed']):
        return "Transaction Performance"
    if any(word in text for word in ['interface', 'look', 'design', 'ui', 'navigation']):
        return "UI & Design"
    if any(word in text for word in ['help', 'support', 'call', 'service', 'chat']):
        return "Customer Support"
    return "General Feedback"

def run_task_2():
    df = pd.read_csv('data/processed/cleaned_reviews.csv')
    
    print(f"Processing {len(df)} reviews...")
    
    # 1. Advanced Sentiment Analysis
    # We truncate to 512 tokens because BERT has a limit
    results = sentiment_pipeline(df['review'].str[:512].tolist(), truncation=True)
    
    df['sentiment_label'] = [r['label'] for r in results]
    df['sentiment_score'] = [r['score'] for r in results]
    
    # 2. Thematic Analysis
    df['identified_theme'] = df['review'].apply(get_theme)
    
    # 3. Save Results
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/final_analysis.csv', index=False)
    
    print("\n--- Task 2 Summary ---")
    print(df.groupby(['bank', 'identified_theme']).size().unstack(fill_value=0))
    print("\nFinal analysis saved to data/processed/final_analysis.csv")

if __name__ == "__main__":
    run_task_2()