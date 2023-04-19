FROM python:3.10.6

ENV DockerHome=/home/app/visitsapp

RUN mkdir -p $DockerHome
WORKDIR $DockerHome

RUN pip install --upgrade pip

COPY . $DockerHome

RUN pip install -r requirements.txt

EXPOSE 8000

#RUN python manage.py makemigrations
#RUN python manage.py migrate
CMD python manage.py migrate;python manage.py runserver 0.0.0.0:8000
