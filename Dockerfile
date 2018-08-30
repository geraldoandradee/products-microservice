FROM python:3.7-alpine

RUN apk update
RUN apk upgrade
RUN apk add curl

WORKDIR /app
COPY . .

ENV FLASK_APP=app.py

RUN if [ "$FLASK_ENV" = "development" ]; then pip install -r requirements/dev.txt; else pip install -r requirements/prod.txt; fi

EXPOSE 5000

CMD ["flask", "run"]