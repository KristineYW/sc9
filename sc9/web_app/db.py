from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    maxplayers = db.Column(db.Integer)

    def __repr__(self):
        return f"<Game {self.id} {self.name}>"
