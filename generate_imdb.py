import os
import urllib.request
import tarfile
import pandas as pd

def download_and_extract():
    url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
    file_path = "data/aclImdb_v1.tar.gz"
    extract_path = "data/aclImdb"

    if not os.path.exists("data"):
        os.mkdir("data")

    if not os.path.exists(extract_path):
        print("Downloading IMDb dataset...")
        urllib.request.urlretrieve(url, file_path)

        print("Extracting...")
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path="data")

        print("IMDb data downloaded and extracted.")
    else:
        print("IMDb data already exists.")

def collect_reviews(folder):
    data = []
    for label in ["pos", "neg"]:
        path = os.path.join(folder, label)
        for filename in os.listdir(path):
            with open(os.path.join(path, filename), encoding='utf-8') as f:
                text = f.read().replace('\n', ' ')
                data.append((label, text))
    return data

def save_to_csv():
    reviews = collect_reviews("data/aclImdb/train")
    df = pd.DataFrame(reviews, columns=["label", "text"])
    df.to_csv("data/imdb_reviews.csv", index=False)
    print("Saved IMDb dataset to data/imdb_reviews.csv")

if __name__ == "__main__":
    download_and_extract()
    save_to_csv()
