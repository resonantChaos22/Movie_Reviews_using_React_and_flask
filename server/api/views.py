#   IMPORTING LIBRARIES
from flask import Blueprint, jsonify, request
from . import db
from .models import Movie


main = Blueprint('main', __name__)  #   fDEFINES THE BLUEPRINT FROM HEREON AFTER

#   Route for adding movies


@main.route('/add_movies', methods=['POST'])   #    DEFINING ROUTE FOR POST
#   Function for adding movies. Has to be same as the route
def add_movies():

    # GETTING DATA AS A JSON AND CONVERTING INTO A DICTIONARY
    movie_data = request.get_json()

    # CREATING MOVIE OBJECT
    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    db.session.add(new_movie)  # PASSING THE MOVIE OBJECT TO THE DATBASE
    db.session.commit()

    return 'Done', 201

#   Route for displaying movies


@main.route('/movies')
#   Function for displaying movies
def movies():
    movies_list = Movie.query.all()   # GIVES AN OBJECT OF MOVIE CLASS
    movies = []

    for movie in movies_list:
        movies.append({
            "title": movie.title,
            "rating": movie.rating,
        })

    return jsonify({'movies': movies})
