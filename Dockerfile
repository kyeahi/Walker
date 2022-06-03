FROM python:3
WORKDIR /code

RUN pip install Django==3.1.3
RUN pip install Django-bootstrap4
RUN pip install kafka-python
RUN pip install hdfs
RUN pip install boto3
RUN pip install awscli

COPY . /code/

CMD python manage.py runserver 0.0.0.0:8000
