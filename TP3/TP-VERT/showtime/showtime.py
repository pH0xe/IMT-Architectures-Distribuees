from ariadne import graphql_sync, load_schema_from_path, QueryType, make_executable_schema, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, render_template, make_response, jsonify, request, url_for, redirect
import resolvers as r

PORT = 3001
HOST = "localhost"

app = Flask(__name__)

type_def = load_schema_from_path('showtime.graphql')
query = QueryType()
query.set_field('showtimes_list', r.showtimes_list)
query.set_field('showtime_with_date', r.showtime_with_date)

showtime = ObjectType('Showtime')

schema = make_executable_schema(type_def, showtime, query)

# get a welcome message
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('playground'), 302)


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
    app.run(host=HOST, port=PORT, debug=True)
