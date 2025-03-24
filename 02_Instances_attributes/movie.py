class Movie:

    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

favorite_movie = Movie('The Count of Mont Cristo', 1998, 4.5)
print(favorite_movie.title)
print(favorite_movie.year)
