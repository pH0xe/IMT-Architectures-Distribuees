import json
import movie_pb2
import movie_pb2_grpc
import grpc
from concurrent import futures

BOOKING_PORT = 3004
SHOWTIME_PORT = 3003
USER_PORT = 3002
MOVIE_PORT = 3001

HOST = "localhost"

class MovieServicer(movie_pb2_grpc.MovieServicer):
    def __init__(self):
        with open('{}/databases/movies.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["movies"]

    def GetMovieByID(self, request, context):
        print("===== GetMovieById =====")

        for movie in self.db:
            if movie['id'] == request.id:
                print("Movie found!")
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'],
                                           id=movie['id'])
        return movie_pb2.MovieData(title="", rating="", director="", id="")

    def GetListMovies(self, request, context):
        print("===== GetListMovie =====")

        for movie in self.db:
            yield movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])

    def GetMovieByTitle(self, request, context):
        print("===== GetMovieByTitle =====")

        for movie in self.db:
            if str(movie['title']) == request.title:
                print('Movie found !')
                return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])
        return movie_pb2.MovieData()

    def CreateMovie(self, request, context):
        print("===== CreateMovie =====")

        movie = self.findMovieById(request.id)
        if movie is not None:
            print('return here movie exist')
            return movie_pb2.MovieData()

        newMovie = {"id": request.id, 'rating': request.rating, 'director': request.director, 'title': request.title};
        self.db.append(newMovie)
        return movie_pb2.MovieData(title=request.title, rating=request.rating, director=request.director, id=request.id)

    def UpdateMovieRating(self, request, context):
        print("===== UpdateMovieRating =====")

        id = request.id
        rating = request.rating
        movie = self.findMovieById(id)
        if movie is None:
            return movie_pb2.MovieData(title="", rating="", director="", id="")

        movie['id'] = rating
        return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])

    def UpdateMovie(self, request, context):
        print("===== UpdateMovie =====")

        movie = self.findMovieById(request.id)
        if movie is None:
            return movie_pb2.MovieData()

        title = request.title
        if not (title is None):
            movie['title'] = title

        rating = request.rating
        if not (rating is None):
            movie['rating'] = rating

        director = request.director
        if not (director is None):
            movie['director'] = director

        return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])

    def DeleteMovie(self, request, context):
        print("===== DeleteMovie =====")

        movie = self.findMovieById(request.id)
        if movie is None:
            return movie_pb2.MovieData()
        self.db.remove(movie)
        return movie_pb2.MovieData(title=movie['title'], rating=movie['rating'], director=movie['director'], id=movie['id'])

    def findMovieById(self, id):
        print("===== findMovieById =====")
        for movie in self.db:
            if id == movie['id']:
                return movie
        return None


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    movie_pb2_grpc.add_MovieServicer_to_server(MovieServicer(), server)
    server.add_insecure_port('[::]:' + str(MOVIE_PORT))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
