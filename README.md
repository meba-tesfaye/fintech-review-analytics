# Fintech Review Analytics

A data analysis project focused on scraping, cleaning, and analyzing customer sentiment for major Ethiopian banks (**CBE**, **BOA**, and **Dashen**) using the Google Play Store reviews.

## 🚀 Project Structure
- `data/`: Local storage for raw and processed CSV files (Git-ignored).
- `notebooks/figures/`: Generated charts and visualizations.
- `scripts/`: Python scripts for the data pipeline.
  - `scrape_reviews.py`: Scrapes ~1,350 reviews using `google-play-scraper`.
  - `preprocess_data.py`: Cleans duplicates and formats dates.
  - `analyze_sentiment.py`: Labels reviews as Positive, Neutral, or Negative.
  - `visualize_results.py`: Generates sentiment distribution and rating charts.

## 🛠️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/meba-tesfaye/fintech-review-analytics.git](https://github.com/meba-tesfaye/fintech-review-analytics.git)