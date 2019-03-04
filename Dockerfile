FROM python:3.6-alpine


LABEL maintainer vhishious@yahoo.com


RUN mkdir -p /mpharma

COPY  . /mpharma


WORKDIR /mpharma


ADD requirements.txt /mpharma/

#RUN pip install -r requirements.txt

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


EXPOSE 8000

CMD ["manage.py runserver 0.0.0.0:8000"]
