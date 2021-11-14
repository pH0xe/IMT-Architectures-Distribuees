import requests
from flask import Flask, render_template, request, jsonify, make_response
import json

app = Flask(__name__)

PORT = 3000
HOST = '127.0.0.1'

# Ajout de variable pour l'accé a l'API IMDB
BASE_URL = 'https://imdb-api.com/fr/API/'
TOKEN = '/k_km5ai6li'

with open('{}/databases/movies.json'.format("."), "r") as jsf:
    moviesLocal = json.load(jsf)["movies"]

# creation de l'url de base
def construct_url(action):
    return BASE_URL + action + TOKEN

# root message
@app.route("/", methods=['GET'])
def home():
    return make_response(""
                         "<h1 style='color:blue'>Welcome to the Movie service!</h1>"
                         "<a href=\"./movies\">Liste des films<a>"
                         "", 200)

# Methode generique de test des requete vers IMDB
def is_request_error(req):
    if req.status_code != 200:
        return True, make_response(jsonify({ 'error': 'Unknow error'}), req.status_code)
    req = req.json()
    if len(req['errorMessage']) != 0:
        return True, make_response(jsonify({'errorMessage': req['errorMessage']}), 418)
    return False, None

# On recupere le top 200 des films sur IMDB
@app.route("/movies", methods=['GET'])
def get_movies():
    movies = requests.get(construct_url('Top250Movies'))
    isError, response = is_request_error(movies)
    if isError:
        return response
    movies = movies.json()
    movies = movies['items']
    # on ajoute le liens pour avoir des detail
    add_link_to_movies(movies, request.url_root)
    return make_response(jsonify(movies), 200)


# Recherche des détatil d'un film sur IMDB avec sont ID
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    url = construct_url('Title') + '/' + movieid
    movie = requests.get(url)
    isError, response = is_request_error(movie)
    if isError:
        return response
    movie = movie.json()
    return make_response(jsonify(movie), 200)


# Recherche des films qui corresponde a un titre sur IMDB
# Renvoie la liste des films + les liens pour accéder au detail de chaque films
@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    found_movies = {}
    if request.args:
        req = request.args
        title = str(req["title"])
        url = construct_url('SearchMovie') + '/' + title
        found_movies = requests.get(url)
    else:
        return make_response(jsonify({'errorMessage': 'No movie title profided'}), 400)

    isError, response = is_request_error(found_movies)
    if isError:
        return response

    found_movies = found_movies.json()
    found_movies = found_movies['results']
    add_link_to_movies(found_movies, request.url_root)
    return make_response(jsonify(found_movies))


def add_link_to_movies(movies, base_url):
    for movie in movies:
        movie['filmDetail'] = "[HTTP GET] " + base_url + "movies/" + movie['id']


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT, debug=True)
