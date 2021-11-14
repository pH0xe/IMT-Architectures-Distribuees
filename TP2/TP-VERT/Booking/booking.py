import json
import booking_pb2
import booking_pb2_grpc
import grpc
from concurrent import futures
import showtime_pb2
import showtime_pb2_grpc

# Fonction pour verifier l'existance d'un filmm dans la programmation d'un jours
def is_booking_available(date, movie):
    # On ouvre un channel vers showtime puis on get toute les programmation de la journée passé en parametre
    with grpc.insecure_channel('localhost:3003') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)
        times = stub.GetTimesByDate(showtime_pb2.Date(date=date))

    for mv in times.movies:
        if movie == mv:
            return True
    return False


# Fonction pour verifier si une reservation a deja été faite par un user
# Pour les reservations d'un users on regarde chaque date.
# Si la date correspond a la date passé en argument on regarde chaque film de ce jours.
# Si ce film correspond a celui passé en parametre on renvoie True. False Sion
# Amelioration possible: Fusion avec les methode bookingHasDate et HasBooking
def isBookingAlreadyMade(booking, date, movie):
    for dt in booking:
        if dt['date'] == date:
            for mv in dt['movies']:
                if mv == movie:
                    return True
    return False


# Fonction pour verifié si un utilisateur a deja la date passé en parametre dans ses reservation
# renvoie un Tuple (boolean, dict)
# True + l'objet dates si l'user a deja la dates
# False + None sinon
def bookingHasDate(booking, date):
    for dt in booking['dates']:
        if dt['date'] == date:
            return True, dt
    return False, None


# Fonction permettant de verifier si un objet dates possede deja le film passé en paramettre ou non
def haBooking(dates, p_movie):
    for mv in dates['movies']:
        if mv == p_movie:
            return True
    return False


class BookingServicer(booking_pb2_grpc.BookingServicer):
    def __init__(self):
        with open('{}/databases/bookings.json'.format("."), "r") as jsf:
            self.bookings = json.load(jsf)["bookings"]

    # Fonction qui renvoie la liste complete des reservation
    def getBookings(self, request, context):
        for booking in self.bookings:
            yield booking_pb2.BookingData(userid=booking['userid'], dates=booking['dates'])

    # Fonction qui renvoie les reservation pour un user
    def getBookingForUser(self, request, context):
        for booking in self.bookings:
            if booking['userid'] == request.userid:
                return booking_pb2.BookingData(userid=booking['userid'], dates=booking['dates'])
        return booking_pb2.BookingData(userid="", dates="")

    # Fonction qui êrmet la Création d'une reservation pour un user donné
    # renvoie un ReturnInfoBooking (boolean d'erreur + message d'info)
    def addBookingByUser(self, request, context):
        # on recupere les info du user et du film
        p_userId = request.userid
        p_date = request.date
        p_movie = request.movie
        # On verifie la possibilité de la reservation
        if not is_booking_available(p_date, p_movie):
            return booking_pb2.returnInfoBooking(error=True, message='their is no available movie at this date')

        # on verifie si l'user existe dans la bdd booking
        # Si il n'existe pas on le créé
        # booking contient les reservation pour un user
        exist, booking = self.userAlreadyExist(p_userId)
        if not exist:
            booking = self.createNewUser(p_userId)
        # on verifie si le user a deja une reservation pour cette dates
        hasDate, dates = bookingHasDate(booking, p_date)

        # Si il n'a pas de date alors on créé l'objet et on l'ajoute a la bdd. Puis fin de la fonction
        if not hasDate:
            arr = [p_movie]
            booking['dates'].append({'date': p_date, 'movies': arr})
            return booking_pb2.returnInfoBooking(error=False, message='Booking successfully added')

        # Traitement du cas ou le user a deja fais la reservation, erreur + message, fin de la fonction
        if haBooking(dates, p_movie):
            return booking_pb2.returnInfoBooking(error=True, message='Booking already made')

        # on ajoute le film a la liste des film reservé, fin de la fonction
        dates['movies'].append(p_movie)
        return booking_pb2.returnInfoBooking(error=False, message='Booking successfully added')

    # Fonction permettant de verifie si le users existe dans la bdd booking
    # Renvoie True + les reservation du user si il existe
    # Renvoie False + None si il n'xiste pas
    def userAlreadyExist(self, userId):
        for booking in self.bookings:
            if userId == booking['userid']:
                return True, booking
        return False, None

    # Fonction pour la création d'un nouveau User dans la bdd booking
    def createNewUser(self, userId):
        booking = { 'userid': userId, 'dates': []}
        self.bookings.append(booking)
        return booking


# on lance le server grpc
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3004')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
