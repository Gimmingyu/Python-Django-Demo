# Python-Django-Demo

[Django Documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

## Installation

```
python -m pip install Django

python -m django version
>> 4.1.2
```

## Create a new Django APP

```
django-admin startproject app
```

<img src="https://user-images.githubusercontent.com/79045153/195593594-3178c423-4f51-4072-bb0d-af3f290bd0d2.png" width=200 heighy=200 />


### manage.py

A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

### app/*.py

The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

### app/__init__.py

An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

### app/settings.py

Settings/configuration for this Django project. Django settings will tell you all about how settings work.

### app/urls.py

The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

### app/asgi.py

An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/) for more details.

### app/wsgi.py

An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/) for more details.

## Run server

```shell
python manage.py runserver
```

<img src="https://user-images.githubusercontent.com/79045153/195595097-20b0be2d-d8ef-47a9-9c2a-24565e6becce.png" />

Django docs says as follows:


> don’t use this server in anything resembling a production environment.  
> It’s intended only for use while developing.  
> (We’re in the business of making web frameworks, not web servers.)


## Change port

```
$ python manage.py runserver 8080

or 

$ python manage.py runserver 0.0.0.0:8000
```

## Django startapp

```
$ python manage.py startapp polls
```

<img src="https://user-images.githubusercontent.com/79045153/195596827-164ff10b-feb3-41aa-8eac-b9370b4ed9dd.png" width=200 height=200 /><br />


