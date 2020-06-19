  
from flask import Flask


from sc.sprint_challenge.aq_dashboard import DB, APP, migrate

DATABASE_URL = 'sqlite:///db.sqlite3'

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    migrate.init_app(app, DB)

    # app.register_blueprint(APP)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)