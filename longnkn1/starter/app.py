from auth import AuthError, requires_auth
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from models import Actor, Movie, setup_db


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=database_path)
    CORS(app)
    
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers",
                             "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Headers",
                             "GET, POST, PATCH, DELETE, OPTIONS")
        return response

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_all_movies(payload):
        try:
            # Get all movie in database
            movies = Movie.query.all()
            movies_list = [movie.format() for movie in movies]
            return jsonify({ "success": True, "movies": movies_list,}), 200
        except:
            abort(500)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movie(payload):
        response = request.get_json()
        # add information for new movies
        new_title = response.get('title', None)
        new_genre = response.get('genre', None)
        new_producer = response.get('producer', None)
        #Check invalid value
        if not new_title or not new_genre or not new_producer:
            abort(400)       
        # insert new movie into database
        try:
            new_movie = Movie(title=new_title, genre=new_genre,producer=new_producer)
            new_movie.insert()
            return jsonify({
                'success': True,
                'movie': new_movie.format()
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    # Delete movie by id
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def remove_movie(payload, movie_id):
        movie_by_id = Movie.query.get(movie_id)       
        #Check null for movie
        if movie_by_id is None:
            abort(404)
        try:
            movie_by_id.delete()
            return jsonify({
                'success': True,
                'movie_removed': movie_id
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def modify_movie(payload, movie_id):
        movie_by_id = Movie.query.get(movie_id)        
        # Check null
        if not movie_by_id:
            abort(404)
        # Update movie
        try:
            response = request.get_json()
            movie_by_id.title = response.get('title', movie_by_id.title)
            movie_by_id.genre = response.get('genre', movie_by_id.genre)
            movie_by_id.producer = response.get('producer', movie_by_id.producer)
            movie_by_id.update()
            return jsonify({
                'success': True,
                'movie': movie_by_id.format()
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_all_actors(payload):
        # Get actors in database
        try: 
            get_all_actors = Actor.query.all()
            actors = [actor.format() for actor in get_all_actors]            
            return jsonify(
                {"success": True,"actors": actors}), 200
        except:
            abort(500)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actor(payload):
        response = request.get_json()
        new_name = response.get('name', None)
        new_gender = response.get('gender', None)
        new_bio = response.get('bio', None)        
        #Check invalid value 
        if not new_name or not new_gender or not new_bio:
            abort(400)       
        try:
            new_actor = Actor(
                name=new_name,
                gender=new_gender,
                bio=new_bio)
            new_actor.insert()
            return jsonify({
                'success': True,
                'actor': new_actor.format()
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def remove_actor(payload, actor_id):       
        #Get actor by id
        actor_by_id = Actor.query.get(actor_id)
        if not actor_by_id:
            abort(404)
        try:
            # Delete actor
            actor_by_id.delete()
            return jsonify({
                'success': True,
                'actor_removed': actor_id
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def modify_actor(payload, actor_id):
        actor_by_id = Actor.query.get(actor_id)
        # check null
        if not actor_by_id:
            abort(404)
        response = request.get_json()
        new_name = response.get('name', actor_by_id.name)
        new_gender = response.get(
                'gender', actor_by_id.gender)
        new_bio = response.get('bio', actor_by_id.bio)
        # Update actor
        try:
            actor_by_id.name = new_name
            actor_by_id.gender = new_gender
            actor_by_id.bio = new_bio
            
            actor_by_id.update()
            return jsonify({
                'success': True,
                'actor': actor_by_id.format()
            })
        except HTTPException as e:
            raise e
        except:
            abort(500)

    @app.errorhandler(AuthError)
    def auth_error(error):
        return (
            jsonify({
                "success": False,
                "error": error.status_code,
                "message": error.error['description']
            }), error.error
        )

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400)

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404,
                    "message": "Not Found"}), 404,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify({"success": False, "error": 500,
                    "message": "Internal server error"}), 500,
        )
    return app
app = create_app()
if __name__ == '__main__':
    app.run()