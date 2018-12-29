import os, sys
from bottle import route, run, static_file, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

cwd = os.path.join(os.getcwd(), 'views', 'horoscope.tpl')


@route("/")
@view(cwd)
def api_hor():
    date = dt.now()
    x = random()
    return {
        "date" : f"{dt.now().year}-{dt.now().month}-{dt.now().day}"
        }

@route("/api/forecast")
def api_forecast():
    prophecies = generate_prophecies(6, 2)
    return {"prophecies" : prophecies}

# @bottle.route("/api/test")
# def api_test():
#     return {"test": True}

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
