import json
from string import Template

import requests as requests


def openDB():
    with open('{}/databases/bookings.json'.format("."), "r") as rfile:
        bookings = json.load(rfile)
    return bookings['bookings']


def saveDB(bookings):
    bookings = {"bookings": bookings}
    with open('{}/databases/movies.json'.format("."), "w") as wfile:
        json.dump(bookings, wfile)


#################################################
##################### QUERY #####################
#################################################

def bookings_list(_, info):
    bookings = openDB()
    return bookings


def bookings_for_user(_, info, _userId):
    bookings = openDB()
    for b in bookings:
        if b['userid'] == _userId:
            return b

#################################################
################### MUTATION ####################
#################################################

def add_booking_for_user(_, info, _userId, _date, _movie):
    queryTemplate = Template('query {showtime_with_date(_date: "$date") {movies}}')
    query = queryTemplate.substitute(date=_date)

    res = requests.post("http://127.0.0.1:3001/graphql", json={'query': query})
    if res.status_code != 200:
        return
    movies = res.json()['data']['showtime_with_date']['movies']

    for m in movies:
        if m['id'] == _movie:
            return

    # TODO pas encore finis
    pass