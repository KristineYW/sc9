from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import openaq

migrate = Migrate()
APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f"<Air Quality Check Info: {self.id} {self.datetime} {self.value}>"


@APP.route('/')
def root():
    api = openaq.OpenAQ()
    status, body = api.measurements(city='Los Angeles', parameter='pm25')

    utc_datetimes = []
    for i in range(0, 100):
        utc = body['results'][i]['date']['utc']
        utc_datetimes.append(utc)


    values = []
    for j in range(0, 100):
        value = body['results'][j]['value']
        values.append(value)

    return (str(values) + str(utc_datetimes))


# @APP.route('/refresh')
# def refresh():
#     """Pull fresh data from Open AQ and replace existing data."""
#     DB.drop_all()
#     DB.create_all()
#     # TODO Get data from OpenAQ, make Record objects with it, and add to db
#     DB.session.commit()
#     return 'Data refreshed!'
