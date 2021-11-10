import requests as requests
from flask import Flask, make_response, jsonify, request
import json

PORT = 3003
HOST = "0.0.0.0"

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
    return make_response(jsonify(users), 200)

# get a user with an id
@app.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
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
    for user in users:
        if user["id"] == str(user_id):
            users.remove(user)
            return make_response(jsonify(user), 200)
    return make_response("This user id doesn't exist", 400)


# get all watched movie by a user
@app.route("/watched_movies/<user_id>", methods=['GET'])
def get_watched_movies(user_id):
    for user in users:
        if user["id"] == str(user_id):
            watched_movies = []
            booking = requests.get("http://127.0.0.1:3002/bookings/" + user['id'])
            booking = booking.json()
            movies = requests.get("http://127.0.0.1:3000/json")
            movies = movies.json()

            for movie in movies:
                for date in booking["dates"]:
                    for mov in date["movies"]:
                        if mov == movie["id"]:
                            watched_movies.append(movie)

            return make_response(jsonify(watched_movies), 200)
    return make_response("This user id doesn't exist", 400)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
