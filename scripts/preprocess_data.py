import pandas as pd
import os

# Define file paths
raw_data_path = 'data/raw/raw_reviews.csv'
processed_dir = 'data/processed'
output_path = os.path.join(processed_dir, 'cleaned_reviews.csv')

# Ensure the processed data directory exists
os.makedirs(processed_dir, exist_ok=True)

def preprocess_reviews():
    print("--- Starting Data Preprocessing ---")
    
    # 1. Load the raw dataset
    try:
        df = pd.read_csv(raw_data_path)
    except FileNotFoundError:
        print(f"Error: {raw_data_path} not found. Please run the scraper first.")
        return

    initial_count = len(df)
    
    # 2. Remove Duplicates
    # We remove rows where the review text is identical
    df.drop_duplicates(subset=['review'], inplace=True)
    count_after_dupes = len(df)
    
    # 3. Handle Missing Values
    # Drop rows missing the actual review text or the star rating
    df.dropna(subset=['review', 'rating'], inplace=True)
    count_after_missing = len(df)
    
    # 4. Normalize Dates
    # Convert dates to YYYY-MM-DD format as required by the brief
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    # 5. Save the cleaned dataset
    # We only keep the 5 required columns: review, rating, date, bank, source
    required_columns = ['review', 'rating', 'date', 'bank', 'source']
    df_final = df[required_columns]
    
    df_final.to_csv(output_path, index=False)
    
    # Summary Output
    print(f"Initial reviews collected: {initial_count}")
    print(f"Duplicates removed: {initial_count - count_after_dupes}")
    print(f"Rows with missing data removed: {count_after_dupes - count_after_missing}")
    print(f"Final cleaned dataset size: {count_after_missing}")
    print(f"Cleaned data saved to: {output_path}")
    print("--- Preprocessing Complete ---")

if __name__ == "__main__":
    preprocess_reviews()