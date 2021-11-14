from ariadne import graphql_sync, load_schema_from_path, QueryType, ObjectType, make_executable_schema, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, render_template, request, jsonify, make_response, redirect, url_for
import json
import resolvers as r

app = Flask(__name__)

PORT = 3000
HOST = '127.0.0.1'

type_defs = load_schema_from_path('movie.graphql')

# Query
query = QueryType()
query.set_field('movies_list', r.movies_list)
query.set_field('movie_with_id', r.movie_with_id)
query.set_field('movie_with_title', r.movie_with_title)

# Mutation
mutation = MutationType()
mutation.set_field('create_movie', r.create_movie)
mutation.set_field('delete_movie', r.delete_movie)
mutation.set_field('update_movie', r.update_movie)

# Movie
movie = ObjectType('Movie')

# Schema
schema = make_executable_schema(type_defs, movie, query, mutation)


@app.route("/", methods=['GET'])
def home():
    return redirect(url_for('playground'), code=302)

@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT, debug=True)
