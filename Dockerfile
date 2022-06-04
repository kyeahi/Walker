FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install Django==3.1.3
RUN pip install Django-bootstrap4
RUN pip install kafka-python
RUN pip install hdfs
RUN pip install boto3
RUN pip install awscli
RUN pip install gunicorn==20.1.0

COPY . /code/
WORKDIR /code/Django

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
