## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `capstone_project_db` database:
```bash
createdb capstone_project_db
```
Populate the database using the `capstone_project.psql` file provided. From the `backend` folder in terminal run:

```bash
psql capstone_project_db < capstone_project.psql
```

### Run the Server

From within the `./backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.
### RBAC
- Casting assistant permissions:
    "get:actors",
    "get:movies"
- Casting director permissions:
    "delete:actors",
    "get:actors",
    "get:movies",
    "patch:actors",
    "patch:movies",
    "post:actors"
- Executive producer permissions:
    "delete:actors",
    "delete:movies",
    "get:actors",
    "get:movies",
    "patch:actors",
    "patch:movies",
    "post:actors",
    "post:movies"
### TOKEN
- ASSISTANT_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikl2OS1fYkVtY2FkU3lJTzM0eVJTViJ9.eyJpc3MiOiJodHRwczovL2Rldi16ZTFqbmZ4YzZsZnppOHMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTIwMjM3ODY3MTc3MjkwMzAyMyIsImF1ZCI6ImNhcHN0b25lX3Byb2plY3RfYXBpIiwiaWF0IjoxNzI3NTk4NjA2LCJleHAiOjE3Mjc2ODUwMDYsInNjb3BlIjoiIiwiYXpwIjoiR3k4Z2xsU1RvdzV1alFidlFKbjd3ZUdhMkl0cWlEUHUiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ncqhlgS2XJ1TiH74RdGzgMF_fTaIV7dZNaM2Z3qq4om3F0TkPtOEyZsKk4uq68K48ALnwIOFX7DpPMwGD6kcISJQM3Ebs-bjsoRD8D3w3s96LjYscztJQ5EpfSJCoOz1tYzYYSpO8v4EONfpZjWfdinLJISqtqCaIQnD3LIVQkbHPq4WkUDgV_Uhq9xjLoPwkFNbYFO5nIoEYE12FUBbVAnAipoFLG-_wDBHN1s3bVVxwlwonYT12gNYFBHpVWRmzhAOCcolqRmNjIGHLhQEveVH0gvhS8o9LplDjZwTWpLJxP7D78w41udy4w1TxHvBzEM74Wv_5rPaDapeEL9i6w'
- DIRECTOR_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikl2OS1fYkVtY2FkU3lJTzM0eVJTViJ9.eyJpc3MiOiJodHRwczovL2Rldi16ZTFqbmZ4YzZsZnppOHMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTIwMjM3ODY3MTc3MjkwMzAyMyIsImF1ZCI6ImNhcHN0b25lX3Byb2plY3RfYXBpIiwiaWF0IjoxNzI3NTk4NTIxLCJleHAiOjE3Mjc2ODQ5MjEsInNjb3BlIjoiIiwiYXpwIjoiR3k4Z2xsU1RvdzV1alFidlFKbjd3ZUdhMkl0cWlEUHUiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.f74n98gzWBL3ah2uUPr8JxwRa-Qeo0bggaX1ZL_gQiNlhf6SRHKtqfXwcjEi_exZhLf1phDj1FWyRCNeavVJii54mrZfFYDKOW1rOiYcsr5m8e3iVKYwlu44muu3im5biDhoyBZhAe64kYQq9BRPCUa2TaX4I6X774YmHKqeB5AO57vRg0k9Hf5AvBZR0Qp9xeMNayXHUV6Im3TzPAwyTHOEutPpJvexrgurivHsoE6k5AIY7SHoBWuHu52S50KFyh4DJBghKC9FVurOAzIGUZo3Ac948Q0SvqaVLxZfvtOPy5qw8fYWh6RSMu2_a_avTwnUhCcNhi9HkcTVVeHUNA'
- PRODUCER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikl2OS1fYkVtY2FkU3lJTzM0eVJTViJ9.eyJpc3MiOiJodHRwczovL2Rldi16ZTFqbmZ4YzZsZnppOHMwLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNTIwMjM3ODY3MTc3MjkwMzAyMyIsImF1ZCI6ImNhcHN0b25lX3Byb2plY3RfYXBpIiwiaWF0IjoxNzI3NTk4NDEwLCJleHAiOjE3Mjc2ODQ4MTAsInNjb3BlIjoiIiwiYXpwIjoiR3k4Z2xsU1RvdzV1alFidlFKbjd3ZUdhMkl0cWlEUHUiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.A7yrkhY9-5oCn0pNUgy32VH2Pjq6ZaqIOoceohA67SRibub7MwFrtw2IX5cnxIclvcfR49CFiCiI4BietV02nQsa7kH0z8rekNMn27YrMEjjRg0pDLQJhFAWY6pI5mdc2pANXtxWkgtdnEtifIc2yz6Xq1_ON9V7CJsGEajH7GMpHhdgTSvs3puU1rh9ODHtFSL-3liaWeN_3B2CIEYxH7R_pO3Qx1cC5c2TOPs55bazuRt3uaWl7W8QT_Z1O6xwdabO3eovoQ9Z0YGnMYdElteRhp5grezb0YNVMoVHknQKCbcua4_ntOdbNOtBG0lSHtaPZb5AzNeTjRC-nhshOg'

### Expected endpoints and behaviors

### `GET '/actors'`
- Fetch the list of all actors from the server. 
- Request Arguments: None
- Returns: A list of actor objects containing the attributes id, bio, gender and name.

```json
{
    "actors": [
        {
            "bio": "Bio 1",
            "gender": "Male",
            "id": 1,
            "name": "Actor 1"
        },
        {
            "bio": "Bio 2",
            "gender": "Female",
            "id": 2,
            "name": "Actor 2"
        },
        {
            "bio": "Bio 3",
            "gender": "Male",
            "id": 3,
            "name": "Actor 3"
        }
    ],
    "success": true
}
```

### `POST '/actors'`
- post a new actor to the server.
- Request Arguments: An object containing string attributes including bio, gender, and name.
```json
        {
            "name": "Test Actor",  
            "gender": "Female",
            "bio": "This is test data for the actor"
        }
```
- Returns: An object containing the information of the newly added movie, including id, bio, gender, and name.
```json
{
    "actor": {
        "bio": "This is test data for the actor",
        "gender": "Female",
        "id": 4,
        "name": "Test Actor"
    },
    "success": true
}
```

### `PATCH '/actors/<int:actor_id>'`
- Find the actor with the matching ID from the URL and modify that actor's data.
- Request Arguments: An object has at least one of these properties: bio, gender, or name.
```json
        {
            "name": "Edited name",  
            "gender": "Male",
            "bio": "Edited bio"
        }
```
- Returns: An object containing the information of the newly updated movie, including id, bio, gender, and name.

```json
{
    "actor": {
        "bio": "Edited bio",
        "gender": "Male",
        "id": 1,
        "name": "Edited name"
    },
    "success": true
}
```

### `DELETE '/actors/<int:actor_id>'`
- Find and delete the actor whose ID matches the ID in the URL.
- Request Arguments: None
- Returns: An object with an actor_removed property that holds the ID of the recently deleted actor.

```json
{
    "actor_removed": 1,
    "success": true
}
```

### `GET '/movies'`
- Fetch the list of all movies from the server. 
- Request Arguments: None
- Returns: A list of movie objects containing the attributes id, genre, producer and title.

```json
{
    "movies": [
        {
            "genre": "Genre 1",
            "id": 1,
            "producer": "Producer 1",
            "title": "Movie 1"
        },
        {
            "genre": "Genre 2",
            "id": 2,
            "producer": "Producer 2",
            "title": "Movie 2"
        },
        {
            "genre": "Genre 3",
            "id": 3,
            "producer": "Producer 3",
            "title": "Movie 3"
        }
    ],
    "success": true
}
```

### `POST '/movies'`
- post a new actor to the server.
- Request Arguments: An object containing string attributes including bio, gender, and name.
```json
        {
            "name": "Test Actor",  
            "gender": "Female",
            "bio": "This is test data for the actor"
        }
```
- Returns: An object containing the information of the newly added movie, including id, bio, gender, and name.
```json
{
    "actor": 
        {
            "name": "Test Actor",  
            "gender": "Female",
            "id": 4,
            "bio": "This is test data for the actor"
        },
    "success": true
}
```

### `PATCH '/movies/<int:movie_id>'`
- Find the actor with the matching ID from the URL and modify that actor's data.
- Request Arguments: An object has at least one of these properties: bio, gender, or name.
```json
        {
            "name": "Edited name",  
            "gender": "Male",
            "bio": "Edited bio"
        }
```
- Returns: An object containing the information of the newly updated movie, including id, bio, gender, and name.

```json
{
    "actor": 
        {
            "name": "Edited name",  
            "gender": "Male",
            "id": 1,
            "bio": "Edited bio"
        },
    "success": true
}
```

### `DELETE '/movies/<int:movie_id>'`
- Find and delete the actor whose ID matches the ID in the URL.
- Request Arguments: None
- Returns: An object with an actor_removed property that holds the ID of the recently deleted actor.

```json
{
    "actor_removed": 1,
    "success": true
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb capstone_project_db_test
createdb capstone_project_db_test
psql capstone_project_db_test < capstone_project.psql
python test_app.py