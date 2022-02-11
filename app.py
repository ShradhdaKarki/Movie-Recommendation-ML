import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    data =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)'.format(movie_id))
    data= data.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies=[]
    recommended_poster = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
option =st.selectbox('Movie of your Choice', movies['title'].values)

if st.button('Recommend'):
    names, posters=recommend(option)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        #st.text(names[0])
        st.image(posters[0],caption=names[0])
    with col2:
        #st.text(names[1])
        st.image(posters[1],caption=names[1])
    with col3:
        #st.text(names[2])
        st.image(posters[2],caption=names[2])
    with col4:
        #st.text(names[3])
        st.image(posters[3],caption=names[3])
    with col5:
        #st.text(names[4])
        st.image(posters[4],caption=names[4])
    with col6:
        #st.text(names[4])
        st.image(posters[5],caption=names[5])





















