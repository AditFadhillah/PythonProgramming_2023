from movie import Movie

class MovieDatabase:
    def __init__(self):
        self.movies = []

    def get_movie_by_name(self, movie_name):
        for movie in self.movies:
            if movie.title == movie_name:
                return movie
        return None

    def movies_by_name(self, partial_movie_name):
        return [movie for movie in self.movies if partial_movie_name.lower() in movie.title.lower()]

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_movies_from_file(self, file):
        with open(file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines[1:]:  # Skip the header line
            data = line.strip().split(';')
            show_id, movie_type, title, director, country, release_year, rating = data

            # Convert "PG-13" to "PG13" if necessary
            if rating == "PG-13":
                rating = "PG13"

            # Create and add the Movie object to the list
            self.add_movie(Movie(title, director, release_year, rating))

    def __str__(self):
        return f"Movie Database with {len(self.movies)} movies"
