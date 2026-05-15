from google_play_scraper import Sort, reviews
import pandas as pd
import time
import os

# Confirmed App IDs for CBE, BOA, and Dashen
banks = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

# Ensure the raw data directory exists
os.makedirs('data/raw', exist_ok=True)

for bank_name, app_id in banks.items():
    print(f"Starting collection for {bank_name}...")
    
    # Target 450 to ensure we meet the 400 minimum requirement
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=450
    )
    
    for r in result:
        all_reviews.append({
            'review': r['content'],
            'rating': r['score'],
            'date': r['at'],
            'bank': bank_name,
            'source': 'Google Play'
        })
    
    print(f"Successfully collected {len(result)} reviews for {bank_name}.")
    time.sleep(2) # Respectful delay to avoid rate limits

# Save to the local data directory
df = pd.DataFrame(all_reviews)
df.to_csv('data/raw/raw_reviews.csv', index=False)

print("-" * 30)
print(f"DONE! Total reviews collected: {len(df)}")
print("File saved at: data/raw/raw_reviews.csv")