import random
import uuid

import grpc
import movie_pb2
import movie_pb2_grpc


def get_movie_by_id(stub, id):
    movie = stub.GetMovieByID(id)
    print(movie)

def get_list_movies(stub):
    allmovies = stub.GetListMovies(movie_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))

def get_movie_by_title(stub, movie_title_str):
    movie_title = movie_pb2.MovieTitle(title=movie_title_str)
    movie = stub.GetMovieByTitle(movie_title)
    print(movie)

def create_movie(stub, t, d, i, r):
    new_movie = movie_pb2.MovieData(title=t, director=d, id=i, rating=r)
    rep = stub.CreateMovie(new_movie)
    print(rep)

def run():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)

        print("-------------- GetListMovies --------------")
        get_list_movies(stub)

        print("-------------- GetMovieByTitle --------------")
        get_movie_by_title(stub, "The Martian")

        print("-------------- GetMovieByTitle --------------")
        get_movie_by_title(stub, "test")

        print("-------------- CreateMovie --------------")
        randomUUID = str(uuid.uuid4())
        randomRating = random.uniform(0, 10)
        create_movie(stub, "new test film", "new movie director", randomUUID, randomRating)
        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id=randomUUID)
        get_movie_by_id(stub, movieid)


if __name__ == '__main__':
    run()
