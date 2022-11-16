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

Run all specific app tests

```shell
coverage run --source='.' manage.py test app --keepdb
```

Run specific test module

```shell
coverage run --source='.' manage.py test api.tests.serializers.test_seller_serializer --keepdb
```

Run all app's tests

```shell
coverage run --source='.' manage.py test . --keepdb
```

Generate report

```shell
coverage report
```

Generate html report

```shell
coverage html
```

Access html report

```shell
python -m http.server 8080
```

## Swagger

Generate schema

```shell
python manage.py spectacular --file schema.yml
```
