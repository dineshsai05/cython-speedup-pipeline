# cython_version/benchmark_parallel.py
import time
from pipeline_parallel import process_texts_parallel
import os

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "imdb_reviews.csv")
    start = time.time()
    process_texts_parallel(csv_path)
    end = time.time()
    print(f"Time taken (Cython + Multiprocessing): {end - start:.2f} seconds")
