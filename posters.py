# web scrapping of the movie posters
import pandas as pd
import requests
from bs4 import BeautifulSoup
from IPython.display import Image, display
def get_images(title):
    query = title + ' poster'
    url = 'https://www.google.com/search?q=' + query + '&tbm=isch'
    content = requests.get(url).content
    soup = BeautifulSoup(content,'lxml')
    images = soup.findAll('img')
    return display(Image(url=images[1].get('src')))

