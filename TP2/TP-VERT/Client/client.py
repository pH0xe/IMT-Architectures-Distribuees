import random
import uuid

import grpc

import booking_pb2
import booking_pb2_grpc
import movie_pb2
import movie_pb2_grpc
import showtime_pb2
import showtime_pb2_grpc

# Test des fonction movie
def testMovie():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)
        print("\n-------------- GetListMovies --------------")
        get_list_movies(stub)
        print("\n-------------- GetMovieByTitle --------------")
        get_movie_by_title(stub, "The Martian")
        print("\n-------------- CreateMovie --------------")
        create_movie(stub)

def get_movie_by_id(stub, id):
    movie = stub.GetMovieByID(id)
    print(movie)

def get_list_movies(stub):
    allmovies = stub.GetListMovies(movie_pb2.EmptyMovie())
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
        print("\n------ GET TIMES FOR 20151201 ------")
        get_times_by_date(stub, "20151201")
        print("\n------ GET TIMES FOR BAD DATE ------")
        get_times_by_date(stub, "20151200")

def get_list_times(stub):
    times = stub.GetListTimes(showtime_pb2.EmptyShowtime())
    for time in times:
        print(time.date + "\nmovies : \n\t" + '\n\t'.join([str(lst) for lst in time.movies]))

def get_times_by_date(stub, date):
    time = stub.GetTimesByDate(showtime_pb2.Date(date=date))
    print(time)



# Test functions of Booking
def testBooking():
    with grpc.insecure_channel('localhost:3004') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        print("------ GET ALL BOOKINGS ------")
        get_list_bookings(stub)
        print("\n------ GET BOOKING FOR dwight_schrute ------")
        get_bookings_user(stub)

        print("\n------ Create Booking FOR dwight_schrute ------")
        print("------ nouvelle date pour dwight ------")
        create_booking(stub, 'dwight_schrute', '720d006c-3a57-4b6a-b18f-9b713b073f3c', '20151130')

        print("\n------ Create Booking FOR dwight_schrute ------")
        print("------ date existante pour dwight ------")
        create_booking(stub, 'dwight_schrute', '39ab85e5-5e8e-4dc5-afea-65dc368bd7ab', '20151201')

        print("\n------ Create Booking FOR dwight_schrute ------")
        print("------ invalide date ------")
        create_booking(stub, 'dwight_schrute', 'new movie', '000')

        print("\n------ Create Booking FOR julien------")
        create_booking(stub, 'julien', '39ab85e5-5e8e-4dc5-afea-65dc368bd7ab', '20151201')

        print("\n------ GET ALL BOOKINGS ------")
        get_list_bookings(stub)

def get_list_bookings(stub):
    bookings = stub.getBookings(booking_pb2.EmptyBooking())
    for booking in bookings:
        print(booking.userid)
        print(booking.dates)


def get_bookings_user(stub):
    booking = stub.getBookingForUser(booking_pb2.UserID(userid="dwight_schrute"))
    print(booking.userid)  # Too long with dates

def create_booking(stub, userid, movie, date):
    newBooking = booking_pb2.newBooking(userid=userid, movie=movie, date=date)
    msg = stub.addBookingByUser(newBooking)
    print('error : ' + str(msg.error) + '\nmessage: ' + msg.message)


def run():
    print('=========================================================')
    print('========================= MOVIE =========================')
    print('=========================================================')
    testMovie()

    print()
    print('=========================================================')
    print('======================= SHOWTIME ========================')
    print('=========================================================')
    testShowtime()

    print()
    print('=========================================================')
    print('======================== BOOKING ========================')
    print('=========================================================')
    testBooking()


if __name__ == '__main__':
    run()
