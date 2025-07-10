# generate_data.py
import csv, random
from pathlib import Path

WORDS = ["the", "cat", "ran", "fast", "on", "road", "dog", "ate", "food", "blue", "car", "tree", "jumped", "over"]

Path("data").mkdir(exist_ok=True)

with open("data/large_text.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "text"])
    for i in range(1000_000):  # adjust if too slow for your CPU
        sentence = " ".join(random.choices(WORDS, k=random.randint(5, 20)))
        writer.writerow([i, sentence])
