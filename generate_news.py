import os
import pandas as pd
from datasets import load_dataset

def generate_news_dataset():
    print("Downloading HuffPost News Headlines...")
    ds = load_dataset("heegyu/news-category-dataset", split="train")
    print(f"Loaded {len(ds)} rows")

    # Convert to DataFrame
    df = pd.DataFrame({"text": ds["headline"]})
    print(f"Before cleaning: {len(df)} rows")

    # Drop rows with NaN or empty text
    df.dropna(inplace=True)
    df = df[df["text"].str.strip() != ""]
    print(f"🧹 After cleaning: {len(df)} rows")

    # Save to CSV
    os.makedirs("data", exist_ok=True)
    output_path = "data/news_headlines.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    generate_news_dataset()
