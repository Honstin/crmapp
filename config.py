import os
basedir = os.path.join(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgres+psycopg2://postgres:postgres@localhost:5432/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False