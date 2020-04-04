from . import db

#   MOVIE CLASS IS DEFINED FOR DATABASE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)
