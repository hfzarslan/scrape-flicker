import pandas as pd
import urllib
from PIL import Image
import urllib.request

df = pd.read_csv('urls.csv')

Products_list = df["URL"].tolist()
print(Products_list)
for i in range(len(Products_list)):
    if i < len(Products_list):
        urllib.request.urlretrieve(Products_list[i+1], str(i) +'img.jpg')