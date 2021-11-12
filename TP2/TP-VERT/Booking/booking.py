import json
import booking_pb2
import booking_pb2_grpc
import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc

def is_booking_available(date, movie):
    print('================== START is_booking_available ==================')
    with grpc.insecure_channel('localhost:3003') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)
        times = stub.GetTimesByDate(showtime_pb2.Date(date=date))

    for mv in times.movies:
        if movie == mv:
            print('================== END is_booking_available ==================')
            return True
    print('================== END is_booking_available ==================')
    return False


def isBookingAlreadyMade(booking, date, movie):
    for dt in booking:
        if dt['date'] == date:
            for mv in dt['movies']:
                if mv == movie:
                    return True
    return False


def bookingHasDate(booking, date):
    for dt in booking['dates']:
        if dt['date'] == date:
            return True, dt
    return False, None


def haBooking(dates, p_movie):
    for mv in dates['movies']:
        if mv == p_movie:
            return True
    return False


class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('{}/databases/bookings.json'.format("."), "r") as jsf:
            self.bookings = json.load(jsf)["bookings"]

    # Get all bookings in a list
    def getBookings(self, request, context):
        for booking in self.bookings:
            yield booking_pb2.Book(userid=booking['userid'], dates=json.dumps(booking['dates']))

    # Get booking for a specific user
    def getBookingForUser(self, request, context):
        for booking in self.bookings:
            if booking['userid'] == request.userid:
                return booking_pb2.Book(userid=booking['userid'], dates=json.dumps(booking['dates']))
        return booking_pb2.Book(userid="", dates="")

    # Add a booking for a user
    def addBookingByUser(self, request, context):
        print('================== START addBookingByUser ==================')

        p_userId = request.userid
        p_date = request.date
        p_movie = request.movie
        if not is_booking_available(p_date, p_movie):
            print('================== END addBookingByUser ==================')
            return booking_pb2.returnInfo(error=True, message='their is no available movie at this date')

        exist, booking = self.userAlreadyExist(p_userId)
        if not exist:
            booking = self.createNewUser(p_userId)
        hasDate, dates = bookingHasDate(booking, p_date)

        if not hasDate:
            arr = [p_movie]
            booking['dates'].append({'date': p_date, 'movies': arr})
            print('================== END addBookingByUser ==================')
            return booking_pb2.returnInfo(error=False, message='Booking successfully added')

        if haBooking(dates, p_movie):
            print('================== END addBookingByUser ==================')
            return booking_pb2.returnInfo(error=True, message='Booking already made')

        dates['movies'].append(p_movie)
        print('================== END addBookingByUser ==================')
        return booking_pb2.returnInfo(error=False, message='Booking successfully added')


    def userAlreadyExist(self, userId):
        for booking in self.bookings:
            if userId == booking['userid']:
                return True, booking
        return False, None

    def createNewUser(self, userId):
        booking = { 'userid': userId, 'dates': []}
        self.bookings.append(booking)
        return booking


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3004')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
