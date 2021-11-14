import json
import random
import string
import uuid


def openMovieDB():
    with open('{}/databases/movies.json'.format("."), "r") as rfile:
        movies = json.load(rfile)
    return movies['movies']


def saveMovieDB(movies):
    movies = {"movies": movies}
    with open('{}/databases/movies.json'.format("."), "w") as wfile:
        json.dump(movies, wfile)


def isUnique(id):
    movies = openMovieDB()
    for m in movies:
        if m['id'] == id:
            return False
    return True


def randomUID():
    uid = uuid.uuid1()
    while not uid:
        uid = uuid.uuid1()
    return str(uid)


#################################################
##################### QUERY #####################
#################################################

# Renvoi tout les films
def movies_list(_, info):
    movies = openMovieDB()
    return movies


# Renvoi un film avec son id
def movie_with_id(_, info, _id):
    movies = openMovieDB()
    for movie in movies:
        if movie['id'] == _id:
            return movie


# Cherche un film par sont titre
def movie_with_title(_, info, _title):
    movies = openMovieDB()
    for movie in movies:
        if movie['title'] == _title:
            return movie


#################################################
################### MUTATION ####################
#################################################

# Creation d'un film
def create_movie(_, info, _title, _director, _rating):
    newMovie = {
        'id': randomUID(),
        'title': _title,
        'director': _director,
        'rating': _rating
    }
    movies = openMovieDB()
    movies.append(newMovie)
    saveMovieDB(movies)
    return newMovie


def delete_movie(_, info, _id):
    movies = openMovieDB()
    deleted_movie = {}
    for m in movies:
        if m['id'] == _id:
            deleted_movie = m
            movies.remove(m)
    saveMovieDB(movies)
    return deleted_movie


# Mise a jour du film
def update_movie(_, info, _id, _title, _director, _rating):
    movies = openMovieDB()
    newMovie = {}
    for movie in movies:
        if movie['id'] == _id:
            if _title is not None:
                movie['title'] = _title
            if _director is not None:
                movie['director'] = _director
            if _rating is not None:
                movie['rating'] = _rating
            newMovie = movie

    saveMovieDB(movies)
    return newMovie
