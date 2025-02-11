from movie_database import MovieDatabase
from viewer import Viewer
from movie import Movie

class StreamingService:
    def __init__(self, name):
        self.name = name
        self.movie_db = MovieDatabase()
        self.customers = []

    def add_customer(self, viewer):
        self.customers.append(viewer)

    def get_movie(self, movie_title):
        movie = self.movie_db.get_movie_by_name(movie_title)
        if movie:
            return movie
        else:
            print(f"Movie '{movie_title}' not found.")

    def search(self, movie_title):
        movies = self.movie_db.movies_by_name(movie_title)
        if movies:
            print(f"Search results for '{movie_title}':")
            for movie in movies:
                print(movie)
        else:
            print(f"No movies found containing '{movie_title}' in the title.")

if __name__ == "__main__":
    NewNetflix = StreamingService("NewNetflix")
    print(f"Welcome to Streaming Service {NewNetflix.name}\n")

    # Add movies from the netflix_db.csv file
    NewNetflix.movie_db.add_movies_from_file("netflix_db.csv")

    # Create viewers
    John = Viewer("John Cleese", 82)
    Peter = Viewer("Peter Pan", 12)
    Pirate = Viewer("Pirate", 340)

    # Add viewers to the streaming service
    NewNetflix.add_customer(John)
    NewNetflix.add_customer(Peter)

    # Search for movies with Monty Python in their title
    NewNetflix.search("Monty Python")

    # Try to watch movies
    monty_python_movie = NewNetflix.get_movie("Monty Python and the Holy Grail")
    if monty_python_movie:
        print(f"\nWatching {monty_python_movie}.\n")
        for viewer in [John, Peter, Pirate]:
            if viewer in NewNetflix.customers:  # Check if the viewer is in the customers list
                if monty_python_movie.can_watch(viewer.age):
                    print(f"{viewer.name} can watch this movie!")
                else:
                    print(f"{viewer.name} cannot watch this movie!\n")
            else:
                print(f"{viewer.name} is not a customer and cannot watch this movie!\n")

    # Add more actions as needed
