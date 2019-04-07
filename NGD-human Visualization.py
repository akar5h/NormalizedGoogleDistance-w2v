import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import preprocessing

d1 = pd.read_csv('combined.csv')
d2 = pd.read_csv('ngdcalc.csv')

d2.iloc[:,0] = d1.iloc[:,0]

x = d2[['Human (mean)']].values.astype(float)

min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x)

w2vscore = pd.DataFrame(x_scaled)
ngd = d2.iloc[:,3]

plt.scatter(w2vscore,ngd)
plt.xlabel("Scaled Human Mean Similarity")
plt.ylabel("Scaled NGD")
plt.title("Scaled NGD v/s Scaled Human Mean Similarity")
plt.savefig('q1.png')
plt.show()

