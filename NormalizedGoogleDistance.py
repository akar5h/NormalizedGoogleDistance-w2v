
import urllib3
import time
import pandas as pd 
import urllib
from bs4 import BeautifulSoup  
import urllib
import math

dataset = pd.read_csv('combined.csv')
words = {} 

final = dataset.iloc[:,1:3]
final['NGD'] = 0

def NormalizedGoogleDistance(x,y,z):
    lx = math.log2(x)
    ly = math.log2(y)
    lz = math.log2(z)

    N = 25270000000000
    
    ngd = (max(lx,ly)- lz)/(math.log2(N)- min(lx,ly))
    return ngd

def searchCount(w):
    http = urllib3.PoolManager()
    wen = urllib.parse.quote(w)

    r = http.request('GET', "https://www.google.com/search?q=" + wen )

    soup = BeautifulSoup(r.data)

    t = soup.select("#resultStats")
    t = t[0].text
    h = "results" 
    i = t.find(h)
    n = t[6:i]
    n = n.replace(",","")
    n = n.replace(" ", "")
    n = int(n)
    return n

for i in range(len(dataset)):
    w1 = dataset.iloc[i,0]
    w2 = dataset.iloc[i,1]

    w3 = w1 + " "  + w2
    if w1 not in words:
        c1 = searchCount(w1)
        words[w1]=c1
        time.sleep(10)
    else:
        c1 = words[w1]
    
    if w2 not in words:
        c2 = searchCount(w2)
        words[w2]=c2
        time.sleep(10)
    else:
        c2 = words[w2]
    
    if w3 not in words:
        c3 = searchCount(w3)
        words[w3]=c3
        time.sleep(10)
    else:
        c3 = words[w3]
    
    n = NormalizedGoogleDistance(c1,c2,c3)
    final.iloc[i,2]= n
    print(f"Word pair= %s %s %s" %(w1,w2,n))
    if(i%20 == 0):
        time.sleep(60)

final.to_csv(r'output.csv')





    