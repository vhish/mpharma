FROM python:3.6-alpine


LABEL maintainer vhishious@yahoo.com

RUN git clone -q https://github.com/vhish/mpharma.git

WORKDIR mpharma

RUN mkdir -p /mpharma

COPY  . /mpharma


WORKDIR /mpharma


ADD requirements.txt /mpharma/

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["manage.py runserver 0.0.0.0:8000"]
