import numpy as np
import pandas as pd
import subprocess
import csv
from scipy import stats
import matplotlib.pyplot as plt
import requests

dataset = pd.read_csv('combined.csv')
last = dataset
last['w2v'] = 0

for i in range(len(dataset)):
    w1 = dataset.iloc[i,0]
    w2 = dataset.iloc[i,1]
    params = (
        ('w1', w1),
        ('w2', w2),
    )
    response = requests.get('http://127.0.0.1:5000/word2vec/similarity/', params=params)
    last.iloc[i,3] = response

last.to_csv('q3.csv', index=False)


a1 = stats.zscore(np.array(last["Human (Mean)"]))
a2 = stats.zscore(np.array(last['w2v']))
plt.figure(0)
plt.xlabel("Standardized Human (Mean) Scores")
plt.ylabel("Standardized Word2Vec Scores")
plt.suptitle("Comparing Human and Word2Vec scores")
plt.scatter(a1,a2)        
plt.savefig("q3.png")

