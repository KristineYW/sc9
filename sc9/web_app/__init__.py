# from flask import Flask

# from web_app.db import db, migrate
# from web_app.routes.game_routes import game_routes


# DATABASE_URL = "sqlite:///games_kristine.db"


# def create_app():
#     app = Flask(__name__)

#     app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     db.init_app(app)
#     migrate.init_app(app, db)

#     app.register_blueprint(game_routes)

#     return app


# if __name__ == "__main__":
#     my_app = create_app()
#     my_app.run(debug=True)
