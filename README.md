# A minimalistic blog API in Domain Driven Design (a study project)

## Building the containers

```sh
make build
make up
# or
make all # builds, brings containers up, runs tests
```

## API health check:
http://0.0.0.0:5005/healthcheck

## Running the tests

```sh
make test
# or, to run individual test types
make unit
make integration
make e2e
# or, if you have a local virtualenv
make up
pytest tests/unit
pytest tests/integration
pytest tests/e2e
```

## Makefile

There are more useful commands in the makefile, have a look and try them out.

## Virtualenv

Install virtualenv for Python3.7:
```sh
pip3.7 install virtualenv
```

create a virtualenv:
```sh
python3.7 -m virtualenv venv
```

Enter the local virtualenv:<br> 
```sh
. venv/bin/activate
```

Pipe out the current requirements.txt file:<br>
```sh
pip freeze > requirements.txt
```

enable env:
```sh
source venv/bin/activate
```

leave venv:
```sh
deactivate
```

Add new packages:
```sh
pip3 install package_name
pip freeze > requirements.txt
```