from flask import Flask, render_template, make_response, jsonify, request
import json

PORT = 5001
HOST = "localhost"

app = Flask(__name__)

with open('{}/databases/times.json'.format("."), "r") as jsf:
  times = json.load(jsf)["schedule"]

# get a welcome message
@app.route('/', methods=['GET'])
def index():
  return make_response("<h1 style='color:blue'>Welcome to the Showtimes service!</h1>",200)

# get all times
@app.route("/showtimes", methods=['GET'])
def get_all():
  res = make_response(jsonify(times), 200)
  return res

# get all times in a day
@app.route("/showtimes/<date>", methods=['GET'])
def get_by_date(date):

  timesInDay = []

  for time in times:
    if str(time["date"]) == str(date):
      timesInDay.append(time)
  return make_response(jsonify(timesInDay), 200)

if __name__ == "__main__":
  app.run(host=HOST, port=PORT)
