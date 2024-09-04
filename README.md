
# Event-manager Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

<a id="introduction"></a>
## Introduction
Event Manager is an **Django**-based **REST API** project for managing events, with some noticeable features:

- Basic User Registration and Authentication.
- CRUD operations, filtering and search for event models
- Event registration
- Email confirmation of registration for the event
- Containerized in Docker
- API documentation on `http://127.0.0.1:8000/swagger/` or `http://127.0.0.1:8000/redoc/`

<a id="installation"></a>
## Installation with Docker
1. Clone This Project ```git clone https://github.com/NixDi/event-manager.git```
2. cd to project directory ```cd eventmanager```
3. In a project directory - Run the following command to create and start containers for web application: ```docker-compose up --build```
4. Then open your django container exec via docker desktop (find container, click on exec button) or by running this command ```docker exec -it container_id python manage.py migrate``` (you can get container_id with ```docker ps```)
5. Then also createsuperuser in the same exec ```docker exec -it container_id python manage.py createsuperuser```
6. Open your web browser and visit `http://localhost:8000/`

<a id="usage"></a>
## Usage Guide with Postman
This guide will walk you through the process of creating and testing events using Postman.
### Prerequisites
- Postman installed on your machine
- You run the following command ```python -m pip install -r requirements.txt```
- You have set up an SMTP server. To configure SMTP, in settings.py fill it with your information. 
Example: 
```python
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```
- Your Django server is running
### Steps
1. **Register a new user**
    - Open Postman and create a new request.
    - Set the request method to `POST` and the URL to `http://localhost:8000/register/`.
    - In the `Body` tab, select `raw` and `JSON`, then enter your user data in the following format:
        ```json
        {
            "username": "your username",
            "email": "your-email",
            "password": "your-password",
            "password2": "confirm your password"
        }
        ```
    - Send the request. The response should include the details of the user you just registered.

2. **Perform CRUD Operations on Events**
    - **Create an Event**
        - Create a new request.
        - Set the request method to `POST` and the URL to `http://localhost:8000/api/events/`.
        - In the `Body` tab, select `raw` and `JSON`, then enter your event data in the following format:
            ```json
            {
                "title": "Event Title",
                "description": "Event Description",
                "location": "Event Location"
            }
            ```
        - Send the request. The response should include the details of the event you just created.

    - **Read an Event**
        - Create a new request.
        - Set the request method to `GET` and the URL to `http://localhost:8000/api/events/` if you want to see all events or `http://localhost:8000/events/event-id/` if you want to see one specific event.
        - In the `Authorization` tab pick a `Basic auth` and enter username and password of user that you create on the first step.
        - Send the request. The response should include the details of the event.

    - **Update an Event**
        - Create a new request.
        - Set the request method to `PUT` and the URL to `http://localhost:8000/events/event-id/`.
        - In the `Authorization` tab pick a `Basic auth` and enter username and password of user that you create on the first step.
        - In the `Body` tab, select `raw` and `JSON`, then enter your updated event data.
        - Send the request. The response should include the details of the updated event.

    - **Delete an Event**
        - Create a new request.
        - Set the request method to `DELETE` and the URL to `http://localhost:8000/events/event-id/`.
        - In the `Authorization` tab pick a `Basic auth` and enter username and password of user that you create on the first step.
        - Send the request. The response should confirm the deletion of the event.

3. **Search for an Event**
    - Create a new request.
    - Set the request method to `GET` and the URL to `http://localhost:8000/api/event/?search=your-search-query/`.
    - In the `Authorization` tab pick a `Basic auth` and enter username and password of user that you create on the first step.
    - Send the request. The response should include the events that match your search query.

4. **Register for an Event**
    - Create a new request.
    - Set the request method to `POST` and the URL to `http://localhost:8000/api/event/event-id/register/`.
    - In the `Authorization` tab pick a `Basic auth` and enter username and password of user that you create on the first step.
    - Send the request. The response should include status: registered and a confirmation letter will be sent to the email specified during registration in the first step.


