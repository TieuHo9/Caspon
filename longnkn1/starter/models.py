import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
database_path = os.environ.get("DATABASE_URL")

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.create_all()


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=True)

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'bio': self.bio
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    producer = db.Column(db.String, nullable=True)
    genre = db.Column(db.String, nullable=True)

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'producer': self.producer,
            'genre': self.genre
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()