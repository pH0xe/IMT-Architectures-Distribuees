from flask import Flask, render_template, request, jsonify, make_response
import json

app = Flask(__name__)

PORT = 3000
HOST = '127.0.0.1'

with open('{}/databases/movies.json'.format("."), "r") as jsf:
    movies = json.load(jsf)["movies"]


# root message
@app.route("/", methods=['GET'])
def home():
    return make_response(""
                         "<h1 style='color:blue'>Welcome to the Movie service!</h1>"
                         "<a href=\"./json\">Liste des films<a>"
                         "", 200)

# get the complete json file
@app.route("/json", methods=['GET'])
def get_json():
    # res = make_response(jsonify(INFO), 200)
    res = make_response(jsonify(movies), 200)
    return res


# get a movie info by its ID
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            return_val = movie.copy()
            discover_api_get(return_val, request.url_root)
            res = make_response(jsonify(return_val), 200)
            return res
    return make_response(jsonify({"error": "Movie ID not found"}), 400)


# add a new movie
@app.route("/movies", methods=["POST"])
def create_movie():
    req = request.get_json()

    for movie in movies:
        if str(movie["id"]) == str(req["id"]):
            return make_response(jsonify({"error": "movie ID already exists"}), 409)

    return_val = req.copy()
    discover_api_update_create(return_val, request.url_root)
    movies.append(req)
    res = make_response(jsonify(return_val), 200)
    return res


# delete a movie
@app.route("/movies/<movieid>", methods=["DELETE"])
def del_movie(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            return make_response(jsonify({"message": "item deleted"}), 200)

    res = make_response(jsonify({"error": "movie ID not found"}), 400)
    return res


# get a movie info by its name
# through a query
@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    found_movie = {}
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                found_movie = movie

    if not found_movie:
        res = make_response(jsonify({"error": "movie title not found"}), 400)
    else:
        return_val = found_movie.copy()
        discover_api_get(return_val, request.url_root)
        res = make_response(jsonify(return_val), 200)
    return res


# change a movie rating
@app.route("/movies/<movieid>/<rate>", methods=["PUT"])
def update_movie_rating(movieid, rate):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["rating"] = float(rate)
            return_val = movie.copy()
            discover_api_update_create(return_val, request.url_root)
            res = make_response(jsonify(return_val), 200)
            return res

    res = make_response(jsonify({"error": "movie ID not found"}), 201)
    return res


@app.route("/movies/<movieid>", methods=["PUT"])
def update_movie(movieid):
    found_movie = {}
    for movie in movies:
        if str(movie['id']) == str(movieid):
            found_movie = movie
            break

    if not found_movie:
        res = make_response(jsonify({"error": "movie not found"}), 400)
    else:
        if 'title' in request.args:
            found_movie['title'] = request.args['title']
        if 'director' in request.args:
            found_movie['director'] = request.args['director']
        if 'rating' in request.args:
            found_movie['rating'] = float(request.args['rating'])
        return_val = found_movie.copy()
        discover_api_update_create(return_val, request.url_root)
        res = make_response(jsonify(return_val), 200)
    return res


def discover_api_get(movie, base_url):
    movie['deleteLink'] = "[HTTP DELETE] " + base_url + "movies/" + movie['id']
    movie['updateRateLink'] = "[HTTP PUT] " + base_url + "movies/" + movie['id'] + "/{rate}"
    movie['updateLink'] = "[HTTP PUT] " + base_url + "movies/" + movie['id'] + "?title=***&rating=***&director=***"


def discover_api_update_create(movie, base_url):
    movie['filmDetail'] = "[HTTP GET] " + base_url + "movies/" + movie['id']


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)
