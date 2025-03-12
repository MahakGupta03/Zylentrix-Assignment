# User API

A simple REST API built with Django and Django Rest Framework.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/MahakGupta03/Zylentrix-Assignment.git
   cd Zylentrix-Assignment

2. Install dependencies: 
   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the server: 
   ```
   python manage.py runserver
   ```


## API Endpoints

### Create a User

- **URL** - http://127.0.0.1:8000/api/users/
- **Method** - POST
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  }
  ```
### List All Users

- **URL** - http://127.0.0.1:8000/api/users/
- **Method** - GET

### Retrieve a User

- **URL** - http://127.0.0.1:8000/api/users/<id>/
- **Method** - GET


### Update a User

- **URL** - http://127.0.0.1:8000/api/users/<id>/
- **Method** - PUT
  ```json
  {
    "name": "John Updated",
    "email": "john.updated@example.com",
    "age": 31
  }
  ```

### Delete a User

- **URL** - http://127.0.0.1:8000/api/users/<id>/
- **Method** - DELETE

