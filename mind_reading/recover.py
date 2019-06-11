#!/usr/bin/env python3

import numpy as np
import random
from model import chars, load_model

model = load_model('model.h5')

n = model.layers[0].input_length # flag length
k = len(chars)

def mutate(seq, m=1):
    seq = seq.copy()
    for i, j in zip(np.random.randint(n, size=m), np.random.randint(k, size=m)):
        seq[i] = j
    return seq

best_seq = np.random.randint(k, size=n)

while True:
    candidates = np.stack([mutate(best_seq, 1) for _ in range(4096)])

    scores = model.predict(candidates).reshape(-1)
    best_idx = scores.argmax()
    best_seq = candidates[best_idx]
    best_score = scores[best_idx]
    print(''.join(map(chars.__getitem__, best_seq)), best_score)

    if best_score == 1.0:
        break
