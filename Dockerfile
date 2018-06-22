FROM python:3.6.3-alpine3.6

WORKDIR /srv/skycrapper

RUN apk add --no-cache --virtual=.run-deps gcc musl-dev

COPY *requirements* /srv/skycrapper/

RUN pip install --no-cache-dir -r requirements.txt

COPY kw /srv/skycrapper/kw/
COPY db /srv/skycrapper/db

CMD ["gunicorn", "--worker-class", "quart.worker.GunicornWorker", "--workers", \
"2", "--bind", "0.0.0.0:80", "--log-level", "debug", "kw.skycrapper:app"]

LABEL name=skycrapper version=dev
