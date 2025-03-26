class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, new_rating):
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print('Enter a valid rating')



my_movie = Movie('The count of Monte Cristo', 4.5)
print(my_movie.rating)

my_movie.rating = 4.9
print(my_movie.rating)