# Tech
- htmx
- flask
- bootstrap


# Running

Set up a virtual environment
```
python -m venv .venv
source .venv/bin/activate
pip install -e .
```
Run development server locally
```
python3 run.py   
```

set up tailwind, and run
```
npx tailwindcss -i ./tailwind_src/input.css -o ./app/static/main.css --watch
```
## Docker
Run from docker
```
docker build . --tag flask-htmx
docker run -p 5678:5678 flask-htmx
```
or with compose
```
docker compose up
```
