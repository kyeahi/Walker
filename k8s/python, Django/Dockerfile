FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install Django==3.1.3
COPY . /code/

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000
