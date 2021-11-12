import grpc
from flask import Flask, make_response, jsonify, request
import json

import movie_pb2_grpc
import movie_pb2

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


# get all users
@app.route("/users", methods=['GET'])
def get_json():
    print("===== get_json =====")

    return make_response(jsonify(users), 200)


# get a user with an id
@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    print("===== get_user =====")

    for user in users:
        if user["id"] == str(user_id):
            return make_response(jsonify(user), 200)
    return make_response("This user id doesn't exist", 400)


def idAlreadyExist(id):
    for user in users:
        if user["id"] == id:
            return True
    return False


# add a user
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


# delete a user with an id
@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    print("===== delete_user =====")

    for user in users:
        if user["id"] == str(user_id):
            users.remove(user)
            return make_response(jsonify(user), 200)
    return make_response("This user id doesn't exist", 400)


# get all watched movie by a user
@app.route("/watched_movies/<user_id>", methods=['GET'])
def get_watched_movies(user_id):
    print("===== get_watched_movies =====")

    if not idAlreadyExist(user_id):
        return make_response("This user id doesn't exist", 400)

    watched_movies = []
    with grpc.insecure_channel('localhost:' + MOVIE_PORT) as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        userId = movie_pb2.MovieID(id=user_id)
        # TODO request booking grpc
    booking = requests.get("http://127.0.0.1:3002/bookings/" + user_id)
    movies = stub.GetListMovies(movie_pb2.Empty())

    for movie in movies:
        for date in booking.dates:
            for mov in date.movies:
                if mov == movie.id:
                    watched_movies.append(movie)

            return make_response(jsonify(watched_movies), 200)



if __name__ == "__main__":
    app.run(host=HOST, port=USER_PORT, debug=True)
