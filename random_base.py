#Create a function, called randomMovies, that takes in an array of movie strings and returns one of those movies randomly


import random
def random_movie(movies):
    return movies[random.randint(0,len(movies)-1)]
