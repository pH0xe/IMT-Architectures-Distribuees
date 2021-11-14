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


# to test templates of Flask
@app.route("/template", methods=['GET'])
def template():
    return make_response(render_template('index.html', body_text='This is my HTML template for Movie service'), 200)


# Fonction qui renvoie tout les films de la bdd
@app.route("/json", methods=['GET'])
def get_json():
    # res = make_response(jsonify(INFO), 200)
    res = make_response(jsonify(movies), 200)
    return res


# Fonction qui renvoie un film avec un id donné (passé en path)
# Si non trouvé renvoie une erreur 400
@app.route("/movies/<movieid>", methods=['GET'])
def get_movie_byid(movieid):
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            return_val = movie.copy()
            discover_api_get(return_val, request.url_root)
            res = make_response(jsonify(return_val), 200)
            return res
    return make_response(jsonify({"error": "Movie ID not found"}), 400)


# Fonction qui permet l'jout d'un film
# Les info du film sont passé dans le body de la requete
# retourne le film qui a été ajouté avec en plus les liens de découverte de l'API
@app.route("/movies", methods=["POST"])
def create_movie():
    req = request.get_json()

    # on verifie si le film n'existe pas deja dans la bdd
    for movie in movies:
        if str(movie["id"]) == str(req["id"]):
            return make_response(jsonify({"error": "movie ID already exists"}), 409)

    # on copie les données dans une nouvelle structure pour pouvoir ajouter les liens de decouverte sans modifier la bdd
    return_val = req.copy()
    discover_api_update_create(return_val, request.url_root)
    movies.append(req)
    res = make_response(jsonify(return_val), 200)
    return res


# Suppression d'un film
# renvoie un json avec un message ou une erreur
@app.route("/movies/<movieid>", methods=["DELETE"])
def del_movie(movieid):
    # Cherche le film puis le delete
    # (Amélioration possible: extraction de la methode de recherche utilisé dans plusieurd fonction)
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movies.remove(movie)
            return make_response(jsonify({"message": "item deleted"}), 200)

    res = make_response(jsonify({"error": "movie ID not found"}), 400)
    return res


# Fonction qui cherche un film par sont titre passé dans le body
# renvoie le film avec les liens de decouverte en cas de succées
# un message d'erreur sinon
@app.route("/moviesbytitle", methods=['GET'])
def get_movie_bytitle():
    found_movie = {}
    # Recherche du film et traitement des erreurs
    if request.args:
        req = request.args
        for movie in movies:
            if str(movie["title"]) == str(req["title"]):
                found_movie = movie

    if not found_movie:
        res = make_response(jsonify({"error": "movie title not found"}), 400)
    else:
        # Ajout des liens de découvertes
        return_val = found_movie.copy()
        discover_api_get(return_val, request.url_root)
        res = make_response(jsonify(return_val), 200)
    return res


# Fonction permettant de mettre a jours une note
# les parametre movieid et rate sont passé dans le path
# renvoie un message d'erreur ou le film modifier avec les liens de découverte
@app.route("/movies/<movieid>/<rate>", methods=["PUT"])
def update_movie_rating(movieid, rate):
    # Recherce du film, modification de la note, copie et ajout des liens
    for movie in movies:
        if str(movie["id"]) == str(movieid):
            movie["rating"] = float(rate)
            return_val = movie.copy()
            discover_api_update_create(return_val, request.url_root)
            res = make_response(jsonify(return_val), 200)
            return res

    res = make_response(jsonify({"error": "movie ID not found"}), 201)
    return res


# Fonction qui met a jours de facon generique un films.
# les parametre sont tous passé en argument dans le path et peuvent etre tous null
@app.route("/movies/<movieid>", methods=["PUT"])
def update_movie(movieid):
    found_movie = {}
    # Recherche du film et traitement des erreurs
    for movie in movies:
        if str(movie['id']) == str(movieid):
            found_movie = movie
            break

    if not found_movie:
        res = make_response(jsonify({"error": "movie not found"}), 400)
    else:
        # On teste chaque arguments et on le modifie si il est presents
        if 'title' in request.args:
            found_movie['title'] = request.args['title']
        if 'director' in request.args:
            found_movie['director'] = request.args['director']
        if 'rating' in request.args:
            found_movie['rating'] = float(request.args['rating'])
        # on ajoute les liens de decouvertel
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
