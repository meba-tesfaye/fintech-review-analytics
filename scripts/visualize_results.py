import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
input_path = 'data/processed/sentiment_reviews.csv'
output_dir = 'notebooks/figures'
os.makedirs(output_dir, exist_ok=True)

# Load data
df = pd.read_csv(input_path)

# Set style for a professional look
sns.set_theme(style="whitegrid")

print("Generating visualizations...")

# 1. Sentiment Distribution by Bank
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='bank', hue='sentiment', palette='magma')
plt.title('Sentiment Analysis: CBE vs BOA vs Dashen')
plt.xlabel('Bank')
plt.ylabel('Number of Reviews')
plt.legend(title='Sentiment')
plt.savefig(f'{output_dir}/sentiment_distribution.png')
plt.close()

# 2. Average Rating per Bank
plt.figure(figsize=(8, 5))
avg_ratings = df.groupby('bank')['rating'].mean().sort_values(ascending=False)
avg_ratings.plot(kind='bar', color=['#4CAF50', '#FFC107', '#2196F3'])
plt.title('Average User Rating by Bank')
plt.ylabel('Score (1-5)')
plt.xticks(rotation=0)
plt.savefig(f'{output_dir}/average_ratings.png')
plt.close()

print(f"Success! Charts saved in: {output_dir}")