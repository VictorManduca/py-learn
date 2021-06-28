<h1 align="center">Py Learn</h1>
<p align="center">Repo to learn python with Django Rest Framework</p>

## Libs
- Python
- Django
- Django Rest Framework

## Instructions (step-by-step)
1) Clone the project
2) Run in the terminal: `python3 -m venv env` to create a environment to run python
3) `pip install -r requirements.txt` to install the dependencies
4) `python manage.py migrate` to run all migrations
5) `python manage.py runserver` to run the server

## URLs
- /users  
  - GET: retrieve all users
  - GET (with ID): retrieve all data from a especific user
  - POST: create a user
  - PUT (with ID): update a user
  - DELETE (with ID): delete a user
