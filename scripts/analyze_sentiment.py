import pandas as pd
import os

# Define file paths
input_path = 'data/processed/cleaned_reviews.csv'
output_path = 'data/processed/sentiment_reviews.csv'

def label_sentiment(rating):
    if rating >= 4:
        return 'Positive'
    elif rating == 3:
        return 'Neutral'
    else:
        return 'Negative'

def run_analysis():
    print("--- Starting Sentiment Analysis ---")
    
    # Load the cleaned data
    df = pd.read_csv(input_path)
    
    # Apply the sentiment logic
    df['sentiment'] = df['rating'].apply(label_sentiment)
    
    # Save the updated dataset
    df.to_csv(output_path, index=False)
    
    # Display the breakdown
    print("Sentiment Breakdown:")
    print(df['sentiment'].value_counts())
    print(f"\nAnalyzed data saved to: {output_path}")
    print("--- Analysis Complete ---")

if __name__ == "__main__":
    run_analysis()