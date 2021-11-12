import json
import booking_pb2
import booking_pb2_grpc
import grpc
from concurrent import futures
#import showtime_pb2
#import showtime_pb2_grpc

def is_booking_available(dates):

    """
    with grpc.insecure_channel('localhost:3003') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)
        times = stub.GetTimesByDate(showtime_pb2.Date(date=booking["date"]))

    for date in dates:
        date = date.json()
        for movie in times['movies']:
            if str(movie) == booking['movieid']:
                return True
    """
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
        # TODO try to do something
        # Bug car showtime renvoie des tableaux de caractères
        return


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3004')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
