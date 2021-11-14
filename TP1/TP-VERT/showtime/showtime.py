from flask import Flask, render_template, make_response, jsonify, request
import json

PORT = 3001
HOST = "localhost"

app = Flask(__name__)

with open('{}/databases/times.json'.format("."), "r") as jsf:
  times = json.load(jsf)["schedule"]

# get a welcome message
@app.route('/', methods=['GET'])
def index():
  return make_response("<h1 style='color:blue'>Welcome to the Showtimes service!</h1>",200)

# fonction qui renvoie toute les programations
@app.route("/showtimes", methods=['GET'])
def get_all():
  res = make_response(jsonify(times), 200)
  return res

# cherche et renvoie toute les programmation pour une journée donnée (passé dans le path)
# en cas d'erreur renvoie un message d'erreur
@app.route("/showtimes/<date>", methods=['GET'])
def get_by_date(date):

  for time in times:
    if str(time["date"]) == str(date):
      return make_response(jsonify(time), 200)
  return make_response("No movie for this date", 400)

if __name__ == "__main__":
  app.run(host=HOST, port=PORT)
