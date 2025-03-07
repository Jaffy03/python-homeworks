import requests
import random

api = '974649a51e8b16c7aec9992f5f7bd347'
base_url = 'https://api.themoviedb.org/3'

def fetch_genres():
    url = f"{base_url}/genre/movie/list?api_key={api}"
    data = requests.get(url)
    if data.status_code == 200:
        return data.json()['genres']
    else: 
        print(f"Failed to fetch genres. Status code: {response.status_code}")
        return []
    
def fetch_movies_by_genre(genre_id):
    url = f"{base_url}/discover/movie?api_key={api}&with_genres={genre_id}"
    data = requests.get(url)
    if data.status_code == 200:
        return data.json()['results']
    else:
        print(f"Failed to fetch movies. Status code: {data.status_code}")
        return []

def recommend_random_movie(genre_name):
    genres = fetch_genres()
    if not genres:
        return
    
    genre_id = None
    for genre in genres:
        if genre['name'].lower() == genre_name.lower():
            genre_id = genre['id']
            break
    if not genre_id:
        print("Genre not found")
        return
    
    movies = fetch_movies_by_genre(genre_id)
    if not movies:
        print("No movies found for genre")
        return 
    
    random_movie = random.choice(movies)
    print(f"Recommended movie in '{genre_name}':")
    print(f"Title: {random_movie['title']}")
    print(f"Overview: {random_movie['overview']}")
    print(f"Release Date: {random_movie['release_date']}")
    print(f"Rating: {random_movie['vote_average']}")
    

genre_name = input("Enter a movie genre: ")
recommend_random_movie(genre_name)


            