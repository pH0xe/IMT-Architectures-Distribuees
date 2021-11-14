from ariadne import graphql_sync, load_schema_from_path, QueryType, MutationType, ObjectType, make_executable_schema
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, make_response, jsonify, request, redirect, url_for
import resolvers as r

PORT = 3002
HOST = "localhost"

app = Flask(__name__)

type_def = load_schema_from_path('booking.graphql')

query = QueryType()
query.set_field('bookings_list', r.bookings_list)
query.set_field('bookings_for_user', r.bookings_for_user)

mutation = MutationType()
mutation.set_field('add_booking_for_user', r.add_booking_for_user)

booking = ObjectType('Booking')
date = ObjectType('Date')

schema = make_executable_schema(type_def, booking, date, query, mutation)

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
