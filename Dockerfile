FROM python:3.8-alpine3.10

ENV TZ=Europe/Moscow

WORKDIR /usr/src/app

RUN set -ex \
    && addgroup -g 82 -S www-data \
    && adduser -u 82 -D -S -G www-data www-data \
    && apk add --upgrade --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        make

COPY . /usr/src/app

RUN set -ex \
    && pip install -r /usr/src/app/requirements.txt --no-cache-dir \
    && apk del .build-deps gcc libc-dev make \
    && chown -R www-data:www-data /usr/src/app