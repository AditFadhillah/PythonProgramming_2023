from rating import Rating

class Movie:
    def __init__(self, title, director, release_year, rating):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.rating = Rating[rating]

    def can_watch(self, age):
        return age >= self.rating.value

    def __str__(self):
        return f"{self.title}, directed by {self.director}, released in {self.release_year}, rated {self.rating}"
