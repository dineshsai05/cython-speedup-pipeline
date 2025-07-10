# cython_version/pipeline.pyx
# cython: language_level=3, boundscheck=False, wraparound=False, nonecheck=False

import pandas as pd
from cpython.dict cimport PyDict_Keys

def process_texts(str file_path):
    cdef list results = []
    cdef dict counts, norm
    cdef list tokens, keys
    cdef str text, word
    cdef int i, n
    cdef double total, freq

    df = pd.read_csv(file_path)

    for text in df['text']:
        tokens = text.strip().split()
        counts = {}
        for word in tokens:
            counts[word] = counts.get(word, 0) + 1

        total = 0
        for freq in counts.values():
            total += freq

        norm = {}
        keys = list(counts.keys())
        n = len(keys)

        for i in range(n):
            word = keys[i]
            norm[word] = counts[word] / total

        results.append(norm)

    return results
