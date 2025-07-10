# cython_version/pipeline_parallel.pyx
# cython: language_level=3, boundscheck=False, wraparound=False

import pandas as pd
from multiprocessing import Pool

# 🚨 This function stays as plain Python to work with multiprocessing
def process_single_text(text):
    tokens = text.strip().split()
    counts = {}
    for word in tokens:
        counts[word] = counts.get(word, 0) + 1

    total = sum(counts.values())
    if total == 0:
        return {}

    norm = {word: freq / total for word, freq in counts.items()}
    return norm

# Parallelized version of process_texts
def process_texts_parallel(str file_path):
    df = pd.read_csv(file_path)
    texts = df['text'].tolist()

    with Pool() as pool:
        results = pool.map(process_single_text, texts)

    return results
