FROM python:3
WORKDIR /code

RUN pip install Django==3.1.3
RUN pip install Django-bootstrap4
RUN pip install kafka-python
RUN pip install hdfs

CMD ls -al
COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000


