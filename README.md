# Intro
The motivation for this project was to create a data visualisation website without relying on large Javascript frameworks such as `React` or `Angular`; instead, the behaviour of a single page application was implemented where needed with `htmx`. A server running Python renders various bits of `HTML`, and these are inserted into the webpage when the user takes actions like clicking a button. This is known as server-side rendering. One of the main benefits to using the technologies demo'd in this project is they simplify the development process as there is no build step and very few dependencies to manage.

There are 20 datasets containing dummy data. Each dataset has 1000 "experiments", and the user is able to select which one of the experiments they wish to view, or they can look at a heatmap that is an aggregation of the dataset. 

![image](https://github.com/jhb123/flask-htmx/blob/main/demo.png?raw=true)


## What this isn't

This is not a demonstration of how to design an API, create perfect templates or manage data in a database.

## Tech
- `htmx`
- `flask`
- `bootstrap`

## Docker
Run from docker
```
docker build . --tag flask-htmx
docker run -p 5678:5678 flask-htmx
```

## Dev

Set up a virtual environment
```
python -m venv .venv
source .venv/bin/activate
pip install -e .
```
The server looks for data in files the location specified `FLASK_DATABASE_PATH` environment variable. It will fall back to `./database` if this is not set
```
export FLASK_DATABASE_PATH=$(pwd)/database
```
Run the script for populating the database.
```
python3 populate_database.py      
```
Run development server locally. It will pick up the data in `FLASK_DATABASE_PATH`
```
python3 run.py   
```


