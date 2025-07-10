# pure_python/benchmark.py
import time
from pipeline import process_texts
import os

if __name__ == "__main__":
    start = time.time()
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "news_headlines.csv")
    process_texts(csv_path)
    end = time.time()
    print(f"Time taken (pure Python): {end - start:.2f} seconds")
