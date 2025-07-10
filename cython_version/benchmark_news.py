import time
from pipeline import process_texts
import os

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "news_headlines.csv")
    start = time.time()
    process_texts(csv_path)
    end = time.time()
    print(f"Time taken (Cython optimized): {end - start:.2f} seconds")
