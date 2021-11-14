import requests as requests
from flask import Flask, make_response, jsonify, request
import json

PORT = 3003
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
    return make_response(jsonify(users), 200)


# Fonction permettant d'obtenir tout les info d'un utilisateur grace a sont id (passé dans le path)
# En cas d'erreur renvoi un message d'erreur et une erreur 400
@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
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
    # recherche de l'utilisateur pour verifier sont existance [Fusion]
    # puis requete sur movie et booking pour obtenir la liste des film et les id des film vu
    for user in users:
        if user["id"] == str(user_id):
            watched_movies = []
            booking = requests.get("http://127.0.0.1:3002/bookings/" + user['id'])
            booking = booking.json()
            movies = requests.get("http://127.0.0.1:3000/json")
            movies = movies.json()

            # Complexité horrible
            # pour chaque film on regarde chaque date et dans cette date on regarde chaque film.
            # Si l'id du film correspond a l'id enregistrer dans booking alors on l'ajoute a la liste des film regardé
            for movie in movies:
                for date in booking["dates"]:
                    for mov in date["movies"]:
                        if mov == movie["id"]:
                            watched_movies.append(movie)
            # on renvoie la liste des film vu
            return make_response(jsonify(watched_movies), 200)
    return make_response("This user id doesn't exist", 400)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
