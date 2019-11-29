# Flask Boilerplate

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
[![Deploy to now](https://deploy.now.sh/static/button.svg)](https://deploy.now.sh/?repo=https://github.com/tko22/flask-boilerplate&env=DATABASE_URL)

The goal of this boilerplate is to allow developers to quickly write their API with code structured to best practices while giving them flexibility to easily add/change features. Here are the problems this is trying to solve:

## Usage

First start a postgres docker container and persist the data with a volume `flask-app-db`:

```
make start_dev_db
```

Another option is to create a postgres instance on a cloud service like elephantsql and connect it to this app. Remember to change the postgres url and don't hard code it in!

Then, start your virtual environment

```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Now, install the python dependencies and run the server:

```
(venv) $ pip install -r requirements.txt
(venv) $ pip install -r requirements-dev.txt
(venv) $ python manage.py recreate_db
(venv) $ python manage.py runserver
```

To exit the virtual environment:

```
(venv) $ deactivate
```

For ease of setup, I have hard-coded postgres URLs for development and docker configurations. If you are using a separate postgres instance as mentioned above, _do not hardcode_ the postgres url including the credentials to your code. Instead, create a file called `creds.ini` in the same directory level as `manage.py` and write something like this:

```
[pg_creds]
pg_url = postgresql://testusr:password@127.0.0.1:5432/testdb
```

Note: you will need to call `api.core.get_pg_url` in the Config file.

For production, you should do something similar with the flask `SECRET_KEY`.

#### Easier setup

I've created a makefile to make this entire process easier but purposely provided verbose instructions there to show you what is necessary to start this application. To do so:

```
$ make setup
```

If you like to destroy your docker postgres database and start over, run:

```
$ make recreate_db
```

This is under the assumption that you have only set up one postgres container that's linked to the `flask-app-db` volume.

#### Using Pipenv

We will be using [pipenv](https://github.com/pypa/pipenv), the recommended package manager for Python. Instead of having to use virtualenv and pip, Pipenv enforces you to use virtual environments, which is something most experienced python developers already do. This allows newer Python developers to already use great practices in the beginning and reduces the barrier to entry. For a better understanding and list of commands you can use with pipenv, look into the [official documentation](https://pipenv.kennethreitz.org/en/latest).

Install Pipenv

```
$ brew install pipenv
```

Activating the Virtual Environment

```
$ pipenv shell
```

Once you are inside the virtual environment, python will have the dependencies (i.e. Flask, SQLAlchemy, etc) installed so you are able to run tests, migrate the database, or start the server! To exit:

```
(flask-boilerplate) bash-3.2$ $ exit
```

Installing and adding other dependencies

```
$ pipenv install <package>
```

The package will be installed to the virtual environment and it will be added to the list of dependencies in Pipfile

To generate a requirements.txt file, which is another common way of managing dependencies, you may run

```
$ pipenv lock -r > requirements.txt
```

### Repository Contents

- `api/views/` - Holds files that define your endpoints
- `api/models/` - Holds files that defines your database schema
- `api/__init__.py` - What is initially ran when you start your application
- `api/utils.py` - utility functions and classes - explained [here](https://github.com/tko22/flask-boilerplate/wiki/Conventions)
- `api/core.py` - includes core functionality including error handlers and logger
- `api/wsgi.py` - app reference for gunicorn
- `tests/` - Folder holding tests

#### Others

- `config.py` - Provides Configuration for the application. There are two configurations: one for development and one for production using Heroku.
- `manage.py` - Command line interface that allows you to perform common functions with a command
- `requirements.txt` - A list of python package dependencies the application requires
- `runtime.txt` & `Procfile` - configuration for Heroku
- `Dockerfile` - instructions for Docker to build the Flask app
- `docker-compose.yml` - config to setup this Flask app and a Database
- `migrations/` - Holds migration files – doesn't exist until you `python manage.py db init` if you decide to not use docker

### MISC

If you're annoyed by the **pycache** files

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

### Additional Documentation

- [Flask](http://flask.pocoo.org/) - Flask Documentation
- [Flask Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/) - great tutorial. Many patterns used here were pulled from there.
- [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - the ORM for the database
- [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) - Deployment using Heroku
- [Learn Python](https://www.learnpython.org/) - Learning Python3
- [Relational Databases](https://www.ntu.edu.sg/home/ehchua/programming/sql/Relational_Database_Design.html) - Designing a database schema
- [REST API](http://www.restapitutorial.com/lessons/restquicktips.html) - tips on making an API Restful
- [Docker Docs](https://docs.docker.com/get-started/) - Docker docs
