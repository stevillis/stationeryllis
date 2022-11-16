# Stationeryllis

A REST API of a Stationery Store app made with Django REST Framework and Postgres.
You can run this project locally or access the [Live Demo](http://stationeryllis.herokuapp.com/) hosted on Heroku using the credentials:

-   User: guest
-   Password: @stationeryllis

### Entity Relationship Diagram

The app was developed by following the ERD
![Entity Relationship Diagram](docs/ERD.jpg?raw=true "Title")

---

## Installation

### Download the project

If you decide to run the project locally, first of all you need to download or clone this repository.

Open the downloaded/cloned folder `stationeryllis` (where the file manage.py is located) with a code editor or terminal to be able to run the following commands.

### Python

Once you have the repository locally, you also must [install Python](https://www.python.org/downloads/) in any version compatible with Python 3.10.

### Virtualenv

You can use the virtual environment manager you like the most, but this project was developed by using [venv](https://docs.python.org/3/library/venv.html) module. After you create your virtualenv, install the project dependencies by using the command

```shell
$ pip install -r requirements.txt
```

### Postgres

It is also necessary to [install Postgres](https://www.postgresql.org/download/) and create a database named `stationeryllis`.

---

## Running the project

1.  Rename the file `.env_example` to `.env` and set the values of `DB_USER` and `DB_PASSWORD` according to your database config. Note: If you changed the default Postgres config, you must also set the values for `DB_HOST` and `DB_PORT`.

2.  Create tables into the already created `stationeryllis` database

    ```shell
    $ python manage.py migrate
    ```

3.  Create a superuser to access Django Admin

    ```shell
    $ python manage.py createsuperuser
    ```

4.  Start the local Django server

    ```shell
    $ python manage.py runserver
    ```

    and access the http://127.0.0.1:8000/ to see the available endpoints or access the Django Admin with the credentials you created in the previous steps.

5.  Accessing the API with an HTTP Client

    To access the API Endpoints locally you must have an Authentication Token.
    To do so, you must follow the steps:

    5.1 Go to Django Admin, using the superuser credentials of step 3

    5.2 Add a new Application in DJANGO OAUTH TOOLKIT app with the following values

    -   Client id: let the auto generated value, but copy it to a secure place, since it will be necessary to create the API `access_token`
    -   Client type: Confidential
    -   Authorization grant type: Resource owner password-based
    -   Client secret: Copy the auto generated secret and paste it in a secure place, since it will be necessary to create the API `access_token`
    -   Name: Set the name of the application. This is the client you will use to communicate with the API, like [Postman](https://www.postman.com/downloads/) and [Insomnia](https://insomnia.rest/download), but you can set any name you want
    -   Keep the other fields with their default value

    5.3 Create the API `access_token` using the HTTP client you are familiar with (Postman, Insomnia or other)

    -   Send a `POST` request to the endpoint `/oauth/token/` with the `body`:

        ```json
        {
            "grant_type": "password",
            "client_id": "The Client id you copied in the previous step",
            "client_secret": "The Client secret you copied in the previous step",
            "username": "The username of user that you created in the step 3",
            "password": "The password of user that you created in the step 3"
        }
        ```

        The response of this request will be something like

        ```json
        {
            "access_token": "nXh3hPiYhaJTHW5yUmA1bg1pzrdXQR",
            "expires_in": 60,
            "token_type": "Bearer",
            "scope": "read write",
            "refresh_token": "GbpwmQUpKaZYzyQDO1wdCGjVJm8BFJ"
        }
        ```

    -   For any endpoint, except `/api/users/`, you must send an access token for all requests, setting the `Authorization` value to `Bearer THE_CREATED_ACCESS_TOKEN` in the request `Headers`.

    -   Using the previous created access token, the `Headers` would have the value
        `Authorization: Bearer nXh3hPiYhaJTHW5yUmA1bg1pzrdXQR`

    5.4 If the access token have expired, you can use the `refresh_token` to create another `access_token` by sending a `POST` request to `/oauth/token/` with the `body`:

    ```json
    {
        "grant_type": "refresh_token",
        "client_id": "The Client id you copied before",
        "client_secret": "The Client secret you copied before",
        "refresh_token": "The refresh_token returned in the response of access_token creation"
    }
    ```

6.  Accessing the API through Swagger UI

    You can access the API endpoints by using the [Swagger UI](http://localhost:8000/api/swagger-ui/) the same way you do with Postman or Insomnia. You have to follow the steps of the section 5 to get the Bearer Token before using this approach.

    The difference here is the way you have to set the Bearer Token:

    -   Click on the `Authorize` button
    -   Set the `Value` to `Bearer THE_CREATED_ACCESS_TOKEN`
    -   Click on the `Authorize` button and then `Close`

    Now you are able to make requests to all endpoints, without having to set the Bearer Token again until it expires (30 days by default).

    The bad side of this approach is that you can't set the `page` parameter when requesting GET method to the endpoints [`/api/customers/`, `/api/customers/`, `/api/sellers/`, `/api/orders/`] like you do in Postman or Insomnia. Therefore, you will always get the first 25 records, since it is the maximum pagination records per page value.

---

## Running tests

You can also run the tests by installing the dev dependencies (you must have the database configured as explained in the previous section)

```shell
$ pip install -r requirements_dev.txt
```

and then running the command

```shell
coverage run --source='.' manage.py test . --keepdb
```

To run specific tests, see the section [dev_commands](./dev_commands.md)
