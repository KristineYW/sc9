from flask import Blueprint, render_template
from web_app.db import db, Game
import bs4
import requests
import numpy as np


game_routes = Blueprint("game_routes", __name__)


@game_routes.route("/add/<game_id>", methods=["GET"])
def fetch_game(game_id=None):
    print(game_id)

    game_url = "https://www.boardgamegeek.com/xmlapi/boardgame/" + game_id
    result = requests.get(game_url)
    soup = bs4.BeautifulSoup(result.text, features='lxml')

    game_id = game_id
    game_name = soup.find('name').text
    game_maxplayers = int(soup.find('maxplayers').text)

    db_game = Game(id=game_id, name=game_name, maxplayers=game_maxplayers)

    db.session.add(db_game)
    db.session.commit()

    return "OK"


@game_routes.route("/", methods=["GET"])
def random_game(game_id=None):

    list_game = list(Game.query.all())
    r_game = np.random.choice(list_game)

    return render_template("home.html",
                           r_game_name=r_game.name,
                           r_game_id=r_game.id,
                           r_max_players=r_game.maxplayers,
                           )


@game_routes.route("/reset")
def reset(game_id=None):
    db.session.query(Game).delete()
    db.session.commit()
    return "deleted it all"


@game_routes.route("/hello")
def hello():
    return "Hello World!"
