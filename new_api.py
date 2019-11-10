# First, you should install flickrapi
# pip install flickrapi

import flickrapi
import urllib
from PIL import Image
import urllib.request
import pandas as pd
# Flickr api access key 
flickr=flickrapi.FlickrAPI('2f1cd3f5826a835a0eca44a96e6d689b', '07c070b3dbadced5', cache=True)


keyword = 'tennis ball'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    print (i)
    
    url = photo.get('url_c')
    
    if url:
        urls.append(url)
        urllib.request.urlretrieve(url, str(i) +'img.jpg')
    
    # get 50 urls


print (urls)
df = pd.DataFrame({'URL': urls})
df.to_csv('urls.csv', index=False)
'''
for i in range(len(urls)):
    if i < len(urls):
        urllib.request.urlretrieve(urls[i+1], str(i) +'img.jpg')
'''