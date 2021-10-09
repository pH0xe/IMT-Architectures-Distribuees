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


# check in showtime db if movie is available
def is_booking_available(booking):
    times = requests.get("http://127.0.0.1:3001/showtimes/" + booking['date'])
    if times.status_code != 200:
        return False

    times = times.json()
    for movie in times['movies']:
        if str(movie) == booking['movieid']:
            return True
    return False


# Adds a booking for the user
@app.route("/bookings/<userid>", methods=['POST'])
def add_booking_byuser(userid):
    body = request.get_json()
    user = {}
    if not body:
        return make_response(jsonify({"error": "booking not provided"}), 409)

    if not is_booking_available(body):
        return make_response(jsonify({"error": "this booking is not available"}), 409)

    # search user:
    for booking in bookings:
        if str(booking['userid']) == str(userid):
            user = booking
            break
    if not user:
        return make_response(jsonify({"error": "user not found"}), 409)

    # check if user already have booking for this date
    for booking in user['dates']:
        if str(booking['date']) == str(body['date']):
            # date exist for the user check if movies already register
            for movie in booking['movies']:
                if str(movie) == str(body['movieid']):
                    return make_response(jsonify({"error": "this booking already exists"}), 409)
            # movie not register add it
            booking['movies'].append(body['movieid'])
            return make_response(jsonify(user), 200)
    # date not yet register add the full object
    body['movies'] = [body['movieid']]
    del body['movieid']
    user['dates'].append(body)
    return make_response(jsonify(user), 200)


@app.route("/bookings", methods=['GET'])
def get_json():
    res = make_response(jsonify(bookings), 200)
    return res


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
