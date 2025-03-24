class Movie:

    id_counter = 1

    def __init__(self, title, year, language, rating):
        self._id = Movie.id_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

        Movie.id_counter += 1


my_movie = Movie('Avengers', 2012, 'English', 4.5)
your_movie = Movie('Snow White', 2025, 'Spanish', 0)

print(my_movie._id)
print(your_movie._id)
