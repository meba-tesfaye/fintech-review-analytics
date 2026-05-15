# Fintech Review Analytics - Ethiopia

A data analysis project focused on scraping, cleaning, and analyzing customer sentiment for major Ethiopian banks (**CBE**, **BOA**, and **Dashen**) using Google Play Store reviews.

## 📊 Methodology & AI Models
- **Scraping:** Used `google-play-scraper` to target CBE, BOA, and Dashen Bank. 
- **Sample:** 450 reviews per bank (**1,350 total**) collected in May 2026.
- **Preprocessing:** Performed deduplication (removing ~325 duplicates) and handled missing values using Pandas. Dates were normalized to `YYYY-MM-DD`.
- **Sentiment Analysis:** Utilized `distilbert-base-uncased-finetuned-sst-2-english`. This Transformer model was chosen over VADER because it understands context and nuances in bank-specific feedback more accurately than rule-based approaches.
- **Thematic Analysis:** Leveraged `spaCy` for tokenization and keyword extraction. Themes (e.g., "Transaction Performance", "UI/UX") were identified by grouping recurring n-grams and significant keywords.

## 🚀 Project Structure
- `.github/workflows/`: CI/CD configuration for automated testing.
- `data/`: Local storage for raw and processed CSV files (**Git-ignored for security**).
- `notebooks/figures/`: Generated charts and visualizations.
- `scripts/`: Modular Python pipeline.
  - `scrape_reviews.py`: Data collection script.
  - `preprocess_data.py`: Data cleaning and normalization.
  - `advanced_analysis.py`: Transformer-based sentiment and thematic labeling.
  - `visualize_results.py`: Chart generation.
- `tests/`: Unit tests for pipeline reliability.

## 🛠️ Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/meba-tesfaye/fintech-review-analytics.git](https://github.com/meba-tesfaye/fintech-review-analytics.git)
   cd fintech-review-analytics