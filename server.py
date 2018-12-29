import os, sys
import bottle
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

cwd = os.path.join(os.getcwd(), 'views', 'horoscope.tpl')


@bottle.route("/")
@bottle.view(cwd)
def api_hor():
    date = dt.now()
    x = random()
    return {
        "date" : f"{dt.now().year}-{dt.now().month}-{dt.now().day}"
        }

@bottle.route("/api/forecast")
def api_forecast():
    prophecies = generate_prophecies(6, 2)
    return {"prophecies" : prophecies}

# @bottle.route("/api/test")
# def api_test():
#     return {"test": True}

bottle.run(
    host="localhost",
    port=8080,
    debug=True,
    autoreload = True
)