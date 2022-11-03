# Stationeryllis

An Stationery Store app made with Django, Postgres and React.
You can run this project locally or access the [Live Demo](http://stationeryllis.herokuapp.com/) hosted on Heroku.

---

## Installation

### Download the project

If you decide to run the project locally, first of all you need to download or clone this repository.

### Python

Once you have the repository locally, you also must [install Python](https://www.python.org/downloads/) in any version compatible with Python 3.10.

### Postgres

It is also necessary to [install Postgres](https://www.postgresql.org/download/) and create a database named `stationeryllis`.

---

## Running the project

Open the downloaded/cloned folder `stationeryllis` (where the file manage.py is located) with a code editor or terminal and run the following commands:

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

    and access the http://127.0.0.1:8000/

5. Django Admin

    To access Django Admin module, you must visit http://127.0.0.1:8000/admin and use the credentials you created in the previous steps.
