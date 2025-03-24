class Movie:

    id_counter = 1

    def __init__(self, title, year, rating):
        self.id = Movie.id_counter 
        self.title = title
        self.year = year
        self.rating = rating

        Movie.id_counter += 1

favorite_movie = Movie('The Count of Mont Cristo', 1998, 4.5)
print(favorite_movie.title)
print(favorite_movie.year)
