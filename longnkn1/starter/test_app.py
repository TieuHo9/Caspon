import json
import os
import unittest
from flask_sqlalchemy import SQLAlchemy
from models import Actor, Movie, setup_db
from dotenv import load_dotenv
from app import create_app

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        load_dotenv()
        self.database_path = os.environ.get("DATABASE_TEST")
        self.assistant_token = os.environ.get("ASSISTANT_TOKEN")
        self.director_token = os.environ.get("DIRECTOR_TOKEN")
        self.producer_token = os.environ.get("PRODUCER_TOKEN")
        self.test_data_actor = {  
            'name': 'Test Actor',  
            'gender': 'Female',
            'bio': 'This is test data for the actor' 
        }
        self.test_data_movie = {  
            'title': 'Test Movie',  
            'producer': 'Test Producer',  
            'genre': 'Male' 
        }
        self.app = create_app({
            "SQLALCHEMY_DATABASE_URI": self.database_path
        })
        self.client = self.app.test_client
        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
    # 4 test case when using user as director role(1 test case for each endpoint)
    # test for movie
    # test get successfully get all movies
    def test_successfully_get_all_movies_as_assistan(self):
        request = self.client().get(
            "/movies",     
            headers={'Authorization': f"Bearer {self.assistant_token}"}
            )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movies"]))
    # test fail to update
    def test_403_error_when_assistant_fails_to_update_movie(self):
        request = self.client().patch(
            "/movies/9999",             
            headers={'Authorization': f"Bearer {self.assistant_token}"}
            )
        data = json.loads(request.data)
        self.assertEqual(data["error"], 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Permission not found.")
        
    # test for actors
    # test fail to add new actor
    def test_403_error_when_assistant_fails_to_add_actor(self):
        request = self.client().post(
            "/actors", 
            json=self.test_data_actor,             
            headers={'Authorization': f"Bearer {self.assistant_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(data["error"], 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Permission not found.")
    # test fail to delete
    def test_403_error_when_assistant_fails_to_remove_actor(self):
        with self.app.app_context():     
            actor = Actor.query.first()
        request = self.client().delete(
            f"/actors/{actor.id}",
            headers={'Authorization': f"Bearer {self.assistant_token}"})
        data = json.loads(request.data)
        self.assertEqual(data["error"], 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Permission not found.")

    # 4 test case when using user as director role(1 test case for each endpoint)
    # test fail to add movie
    def test_403_error_when_director_fails_to_add_movie(self):
        request = self.client().post(
            "/movies", 
            json=self.test_data_movie, 
            headers={'Authorization': f"Bearer {self.director_token}"}
        )
        data = json.loads(request.data)
        data = json.loads(request.data)
        self.assertEqual(data["error"], 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Permission not found.")
    # test successful get all movies
    def test_successfully_get_all_movies_as_director(self): 
        request = self.client().get(
            "/movies", 
            headers={'Authorization': f"Bearer {self.director_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movies"]))
    # test add actors successful
    def test_successfully_add_actor_as_director(self):
        request = self.client().post(
            "/actors", 
            json=self.test_data_actor,  
            headers={'Authorization': f"Bearer {self.director_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["actor"])
    # test delete successful actor
    def test_successfully_remove_actor_as_director(self):
        with self.app.app_context():     
            actor = Actor.query.first()
        request = self.client().delete(
            f"/actors/{actor.id}",  
            headers={'Authorization': f"Bearer {self.director_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["actor_removed"], actor.id)

    # 16 test case when using user as producer role (2 test case for each endpoint)
    def test_successfully_add_movie_as_producer(self):
        request = self.client().post(
            "/movies", 
            json=self.test_data_movie,  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["movie"])

    def test_400_error_when_producer_fails_to_add_movie(self):
        request = self.client().post(
            "/movies", 
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")
    
    def test_successfully_get_all_movies_as_producer(self): 
        request = self.client().get(
            "/movies", 
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movies"]))

    def test_401_error_when_getting_movies(self):
        request = self.client().get("/movies")
        data = json.loads(request.data)
        self.assertEqual(data["error"], 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Authorization header is expected.")

    def test_successfully_modify_movie_as_producer(self):
        with self.app.app_context():
            movie_by_id = Movie.query.first()
        request = self.client().patch(
            f"/movies/{movie_by_id.id}", 
            json=self.test_data_movie,  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["movie"])

    def test_successfully_remove_movie_as_producer(self):
        with self.app.app_context():   
            movie_by_id = Movie.query.first()
        request = self.client().delete(
            f"/movies/{movie_by_id.id}",  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_404_error_when_producer_fails_to_remove_movie(self):
        request = self.client().delete(
            "/movies/99999", 
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_404_error_when_producer_fails_to_modify_movie(self):
        request = self.client().patch(
            "/movies/9999999", 
            json=self.test_data_movie,
            headers={'Authorization': f"Bearer {self.producer_token}"})
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_successfully_add_actor_as_producer(self):
        request = self.client().post(
            "/actors", 
            json=self.test_data_actor,  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIsNotNone(data["actor"])

    def test_400_error_when_producer_fails_to_add_actor(self):
        request = self.client().post("/actors", json={
            "name": "Long Nguyen",
        },  
        headers={'Authorization': f"Bearer {self.producer_token}"})
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")
    
    def test_successfully_get_all_actors_as_producer(self):
        request = self.client().get(
            "/actors",  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["actors"]))

    def test_404_error_when_producer_fails_to_get_all_actors(self):
        request = self.client().get("/actors")
        data = json.loads(request.data)
        self.assertEqual(data["error"], 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Authorization header is expected.")

    def test_successfully_remove_actor_as_producer(self):
        with self.app.app_context():     
            actor_by_id = Actor.query.first()
        request = self.client().delete(
            f"/actors/{actor_by_id.id}",  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data["actor_removed"], actor_by_id.id)

    def test_404_error_when_producer_fails_to_remove_actor(self):
        request = self.client().delete(
            "/actors/1998",
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_successfully_modify_actor_as_producer(self):
        with self.app.app_context():
            actor_by_id = Actor.query.first()
        request = self.client().patch(
            f"/actors/{actor_by_id.id}", 
            json= self.test_data_actor,  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)

    def test_404_error_when_producer_fails_to_modify_actor(self):
        request = self.client().patch(
            "/actors/1998", 
            json=self.test_data_actor,  
            headers={'Authorization': f"Bearer {self.producer_token}"}
        )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
