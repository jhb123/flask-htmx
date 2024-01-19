FROM python:3.11-slim

COPY . /app
WORKDIR /app
RUN pip3 install "."

RUN mkdir -p ./database
ENV FLASK_DATABASE_PATH="./database"

RUN python3 populate_database.py

EXPOSE 5678

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5678", "app:create_app()"]
