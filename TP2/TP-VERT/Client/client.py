import random
import uuid

import grpc
import movie_pb2
import movie_pb2_grpc
import showtime_pb2
import showtime_pb2_grpc
import booking_pb2
import booking_pb2_grpc

# Test functions of Movie

def testMovie():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)
        print("-------------- GetListMovies --------------")
        get_list_movies(stub)
        print("-------------- GetMovieByTitle --------------")
        get_movie_by_title(stub, "The Martian")
        print("-------------- CreateMovie --------------")
        create_movie(stub)

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

def create_movie(stub):
    randomUUID = str(uuid.uuid4())
    randomRating = random.uniform(0, 10)
    movie = stub.CreateMovie(movie_pb2.MovieData(title="new test film", director="new movie director", id=randomUUID, rating=randomRating))
    print(movie)



# Test functions of Showtime

def testShowtime():
    with grpc.insecure_channel('localhost:3003') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)
        print("------ GET ALL TIMES ------")
        get_list_times(stub)
        print("------ GET TIMES FOR 20151201 ------")
        get_times_by_date(stub, "20151201")
        print("------ GET TIMES FOR BAD DATE ------")
        get_times_by_date(stub, "20151200")

def get_list_times(stub):
    times = stub.GetListTimes(showtime_pb2.Empty())
    for time in times:
        print(time.date)

def get_times_by_date(stub, date):
    time = stub.GetTimesByDate(showtime_pb2.Date(date=date))
    print(time)



# Test functions of Booking

def testBooking():
    with grpc.insecure_channel('localhost:3004') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        print("------ GET ALL BOOKINGS ------")
        get_list_bookings(stub)
        print("------ GET BOOKING FOR dwight_schrute ------")
        get_bookings_user(stub)

def get_list_bookings(stub):
    bookings = stub.getBookings(booking_pb2.Empty())
    for booking in bookings:
        print(booking.userid)  # Too long with dates

def get_bookings_user(stub):
    booking = stub.getBookingForUser(booking_pb2.UserID(userid="dwight_schrute"))
    print(booking.userid)  # Too long with dates


def run():
    testMovie()
    testShowtime()
    testBooking()


if __name__ == '__main__':
    run()
