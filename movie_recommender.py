import pickle
import pandas as pd
import numpy as np
with open('dataset.pkl', 'rb') as f:
    df_filtered1 = pickle.load(f)
def recommend_movies(cluster_value):
    print('What do you want to see: Movie or TV series?')
    x=input()
    filtered_movies = df_filtered1[df_filtered1['cluster'] == cluster_value]
    if(x=='Movie'):
        top_movies = filtered_movies[filtered_movies['contentType']=='Movie'].head(10)
    else:
        top_movies = filtered_movies[filtered_movies['contentType']=='TV series'].head(10)
        
    top_movies = filtered_movies.head(10)  # Get the first 10 movies by index
    return top_movies[['dataId', 'title']]