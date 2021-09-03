from bs4 import BeautifulSoup
import urllib.request
import nltk 
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
        freq = nltk.FreqDist(clean_tokens)

#Filtering the code to eliminate the frequency of words less than 5    

newdict = {}
for key,val in freq.items():
    if val>5:
        newdict[key]=val
top10 = sorted(newdict.items(),key=lambda x: x[1], reverse=True)[:10]

#plotting the graph

xs = [x[0] for x in top10]
ys = [x[1] for x in top10]
plt.title("frequency")
plt.plot(xs, ys)