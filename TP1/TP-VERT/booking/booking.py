import requests as requests
from flask import Flask, make_response, jsonify, request
import json

PORT = 3002
HOST = "localhost"

app = Flask(__name__)

with open('{}/databases/bookings.json'.format("."), "r") as jsf:
    bookings = json.load(jsf)["bookings"]


# get a welcome message
@app.route('/', methods=['GET'])
def index():
    return make_response("<h1 style='color:blue'>Welcome to the Booking service!</h1>", 200)


# Methode permettant de verifier la disponibilité d'un film
# Retourne True si le film peut etre reservé
# Retourn False en cas d'erreur ou si le film ne peut pas etre reservé
def is_booking_available(booking):
    # On fait appelle a showtime pour obtenir tout les films du jours
    times = requests.get("http://127.0.0.1:3001/showtimes/" + booking['date'])
    if times.status_code != 200:
        return False

    # Parmis tout les films retourné on regarde si un correspond a celui que l'on souhaite reserver
    times = times.json()
    for movie in times['movies']:
        if str(movie) == booking['movieid']:
            return True
    return False


# Méthode permettant l'ajour d'une reservation.
# Le userid est passé dans le path
# Le Body contient la date et le movieId a enregistrer
@app.route("/bookings/<userid>", methods=['POST'])
def add_booking_byuser(userid):
    body = request.get_json()
    user = {}
    # On verifie la presence du body et on verifie si le film est dispo
    if not body:
        return make_response(jsonify({"error": "booking not provided"}), 409)

    if not is_booking_available(body):
        return make_response(jsonify({"error": "this booking is not available"}), 409)

    # On regarde si le User existe dans booking, si non on arrete la methode
    # (Possibilité d'amelioration: Création du user dans Booking)
    for booking in bookings:
        if str(booking['userid']) == str(userid):
            user = booking
            break
    if not user:
        return make_response(jsonify({"error": "user not found"}), 409)

    # On regarde si le user a deja une reservation pour ce jour
    for booking in user['dates']:
        if str(booking['date']) == str(body['date']):
            # Si la date exist on verifie que le user n'a pas deja reservé ce film
            for movie in booking['movies']:
                if str(movie) == str(body['movieid']):
                    return make_response(jsonify({"error": "this booking already exists"}), 409)
            # Si User n'a pas enregisterr le film alors on le fait et la methode est terminé
            booking['movies'].append(body['movieid'])
            return make_response(jsonify(user), 200)
    # Si la date n'est pas encore enregister on ajoute tout les attribus et la methode est terminé
    body['movies'] = [body['movieid']]
    del body['movieid']
    user['dates'].append(body)
    return make_response(jsonify(user), 200)


# MEthode qui renvoie toutes les réservations
@app.route("/bookings", methods=['GET'])
def get_json():
    res = make_response(jsonify(bookings), 200)
    return res


# Méthode qui renvoie la liste des reservation pour un user donné (passé dans le path)
@app.route("/bookings/<userid>", methods=['GET'])
def get_booking_for_user(userid):
    user = {}
    for book in bookings:
        if str(book['userid']) == str(userid):
            user = book

    if not user:
        return make_response(jsonify({"error": "user not found"}), 400)

    return make_response(jsonify(user), 200)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
