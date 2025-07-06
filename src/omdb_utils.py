import requests

def get_movie_details(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    plot = data.get("Plot", "No plot available.")
    poster = data.get("Poster", "https://via.placeholder.com/200x300?text=No+Image")
    imdb_link = f"https://www.imdb.com/title/{data.get('imdbID', '')}/"
    rating = data.get("imdbRating", "N/A")
    
    return plot, poster, imdb_link, rating
