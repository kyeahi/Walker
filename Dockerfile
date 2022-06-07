FROM python:3

WORKDIR /code

RUN pip install Django==4.0.4
RUN pip install Django-bootstrap4==22.1
RUN pip install kafka-python==2.0.2
RUN pip install hdfs==2.7.0
RUN pip install boto3==1.23.0
RUN pip install awscli==1.25.1
RUN pip install gunicorn==20.1.0
RUN pip install django-environ==0.8.1

COPY . /code/
WORKDIR /code/Django

CMD python manage.py runserver 0.0.0.0:8000
