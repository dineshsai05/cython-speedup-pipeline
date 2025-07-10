import os
import pandas as pd
from datasets import load_dataset

def generate_wiki_dataset():
    print("Downloading Wikipedia dataset (50K rows)...")
    ds = load_dataset("wikipedia", "20220301.en", split="train[:50000]")

    print("Converting to DataFrame...")
    df = pd.DataFrame({"text": ds["text"]})

    output_path = "data/wiki_50k.csv"
    if not os.path.exists("data"):
        os.makedirs("data")

    print(f"Saving to {output_path}...")
    df.to_csv(output_path, index=False)
    print("Done.")

if __name__ == "__main__":
    generate_wiki_dataset()
