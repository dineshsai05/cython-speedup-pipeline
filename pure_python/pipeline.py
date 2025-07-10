# pure_python/pipeline.py
import pandas as pd
from collections import Counter

def tokenize(text):
    return text.strip().split()

def normalize(counts):
    total = sum(counts.values())
    return {word: freq / total for word, freq in counts.items()}

def process_texts(file_path):
    df = pd.read_csv(file_path)
    results = []
    for text in df['text']:
        tokens = tokenize(text)
        counts = Counter(tokens)
        norm = normalize(counts)
        results.append(norm)
    return results