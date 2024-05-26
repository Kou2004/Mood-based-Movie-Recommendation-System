# web scrapping of the movie posters and description,release year along with rating
import pandas as pd
import requests
from bs4 import BeautifulSoup
from IPython.display import Image, display

def get_movie_info(title):
    # Search for movie posters
    query = title + ' poster'
    url = 'https://www.google.com/search?q=' + query + '&tbm=isch'
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    images = soup.findAll('img')
    
    # Display the first image
    display(Image(url=images[1].get('src')))
    
    # Get movie information from IMDb
    imdb_url = f"https://www.imdb.com/find?q={title}&s=tt&ttype=ft&ref_=fn_ft"
    imdb_content = requests.get(imdb_url).content
    imdb_soup = BeautifulSoup(imdb_content, 'html.parser')
    first_result = imdb_soup.find('td', class_='result_text')
    if first_result:
        movie_link = first_result.find('a')['href']
        movie_url = f"https://www.imdb.com{movie_link}"
        movie_page = requests.get(movie_url).content
        movie_soup = BeautifulSoup(movie_page, 'html.parser')
        
        # Extract movie description
        description = movie_soup.find('div', class_='summary_text').text.strip()
        print('Description:', description)
        
        # Extract release year
        title_bar = movie_soup.find('div', class_='title_bar_wrapper')
        release_year = title_bar.find('span', id='titleYear').text.strip('()')
        print('Release Year:', release_year)
        
        # Extract rating
        rating = movie_soup.find('span', itemprop='ratingValue').text
        print('Rating:', rating)
        
    else:
        print('Movie information not found')

