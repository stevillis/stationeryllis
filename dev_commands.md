# Common development commands

## Django

Generate migrations

```shell
python manage.py makemigrations
```

Migrate tables

```shell
python manage.py migrate
```

Shell

```shell
python manage.py shell
```

---

## Tests

### Django

Run tests

```shell
python manage.py test
```

Run tests, keep the database test data and stop in the first failed test

```shell
python manage.py test --keepdb --failfast
```

### Coverage

Run tests with coverage

```shell
coverage run --source='.' manage.py test app --keepdb
```

Access report

```shell
python -m http.server 8080
```
