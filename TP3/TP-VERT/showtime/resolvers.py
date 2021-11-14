import json
import random
import string
import uuid


def openDB():
    with open('{}/databases/times.json'.format("."), "r") as rfile:
        times = json.load(rfile)
    return times['schedule']


def saveDB(times):
    times = {"schedule": times}
    with open('{}/databases/movies.json'.format("."), "w") as wfile:
        json.dump(times, wfile)


#################################################
##################### QUERY #####################
#################################################

# Renvoi tout les films
def showtimes_list(_, info):
    showtimes = openDB()
    return showtimes


def showtime_with_date(_, info, _date):
    showtimes = openDB()
    for s in showtimes:
        if s['date'] == _date:
            return s

#################################################
################### MUTATION ####################
#################################################
