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

1. Rename the file `.env_example` to `.env` and set the values of `DB_USER` and `DB_PASSWORD` according to your database config. Note: If you changed the default Postgres config, you must also set the values for `DB_HOST` and `DB_PORT`.

2. Create tables into the already created `stationeryllis` database

    ```shell
    $ python manage.py migrate
    ```

3. Create a superuser to access Django Admin

    ```shell
    $ python manage.py createsuperuser
    ```

4. Start the local Django server

    ```shell
    $ python manage.py runserver
    ```

    and access the http://127.0.0.1:8000/ to see the available endpoints or access the Django Admin with the credentials you created in the previous steps.

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
