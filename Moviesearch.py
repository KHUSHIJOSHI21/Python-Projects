import requests
def detect_movie(movie):
    api_key= "bb7a2a4e"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie}"
    response=requests.get(url)
    data=response.json()
    if(data.get("Response")=="True"):
        print(f"Title:{data['Title']}")
        print(f"Year:{data['Year']}")
        print(f"Actors:{data['Actors']}")
        print(f"Genre:{data['Genre']}")
        print(f"Plot:{data['Plot']}")
        print(f"IMDB Rating:{data['imdbRating']}")
    else:
        print("Movie not found")
def main():
    print("Welcome to Movie Search App")
    movie=input("Enter the name of the movie")
    detect_movie(movie)
if __name__=='__main__':
    main()