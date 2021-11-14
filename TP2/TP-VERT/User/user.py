import grpc
from flask import Flask, make_response, jsonify, request
import json

from google.protobuf.json_format import MessageToDict

import movie_pb2_grpc
import movie_pb2

import booking_pb2_grpc
import booking_pb2

BOOKING_PORT = 3004
SHOWTIME_PORT = 3003
USER_PORT = 3002
MOVIE_PORT = 3001

HOST = "localhost"

app = Flask(__name__)

with open('{}/databases/users.json'.format("."), "r") as jsf:
    users = json.load(jsf)["users"]


# get a welcome message
@app.route('/', methods=['GET'])
def index():
    return make_response("<h1 style='color:blue'>Welcome to the User service!</h1>", 200)


# Fonction qui renvoie tout les user de la bdd
@app.route("/users", methods=['GET'])
def get_json():
    print("===== get_json =====")

    return make_response(jsonify(users), 200)


# Fonction permettant d'obtenir tout les info d'un utilisateur grace a sont id (passé dans le path)
# En cas d'erreur renvoi un message d'erreur et une erreur 400
@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    print("===== get_user =====")

    for user in users:
        if user["id"] == str(user_id):
            return make_response(jsonify(user), 200)
    return make_response("This user id doesn't exist", 400)


# Fonction permettant de tester qu'un utilisateur exsite
def idAlreadyExist(id):
    for user in users:
        if user["id"] == id:
            return True
    return False


# Fonction permettant l'ajout d'un user dans la bdd
# renvoie le user ajouter en cas de succèes, un message d'erreur sinon
@app.route("/users", methods=['POST'])
def add_user():
    print("===== add_user =====")

    body = request.get_json()
    if not body:
        return make_response(jsonify({"error": "user not provided"}), 409)

    user = body
    if idAlreadyExist(str(user["id"])):
        return make_response(jsonify({"error": "this user id is not available"}), 409)

    users.append(user)
    return make_response(jsonify(user), 200)


# Fonction permettant de supprimer un user grace a sont id (passé dans le path)
@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    print("===== delete_user =====")

    # recherche de l'utilisateur
    # Amelioration possible: fusion de la methode recherche et existance, utilisé dans plusieurs fonctions
    for user in users:
        if user["id"] == str(user_id):
            users.remove(user)
            return make_response(jsonify(user), 200)
    return make_response("This user id doesn't exist", 400)


# Fonction permettant d'obtenir tout les films vu par un utilisateur
@app.route("/watched_movies/<user_id>", methods=['GET'])
def get_watched_movies(user_id):
    print("===== get_watched_movies =====")

    # recherche de l'utilisateur pour verifier sont existance
    if not idAlreadyExist(user_id):
        return make_response("This user id doesn't exist", 400)

    # requete sur movie et booking pour obtenir la liste des film et les id des film vu
    watched_movies = []
    with grpc.insecure_channel('localhost:' + str(MOVIE_PORT)) as channelMovie:
        stub = movie_pb2_grpc.MovieStub(channelMovie)
        movies = stub.GetListMovies(movie_pb2.EmptyMovie())

        with grpc.insecure_channel('localhost:' + str(BOOKING_PORT)) as channelBooking:
            stub = booking_pb2_grpc.BookingStub(channelBooking)
            userId = booking_pb2.UserIDBooking(userid=user_id)
            booking = stub.getBookingForUser(userId)

            # On enregistre tout les id des films vu dans une premiere liste
            for date in booking.dates:
                for mov in date.movies:
                    watched_movies.append(mov)
            # pour chaque film on regarde si il fait partie des film vu.
            # Si il en fait partie on convertie l'objet rpc en Dict python et on l'ajoute a la liste de resultat
            res = []
            for movie in movies:
                if movie.id in watched_movies:
                    mv = MessageToDict(movie)
                    res.append(mv)

            return make_response(jsonify(res), 200)


if __name__ == "__main__":
    app.run(host=HOST, port=USER_PORT, debug=True)
