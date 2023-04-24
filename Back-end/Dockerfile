FROM ubuntu:latest

#Install cron
RUN apt-get update && apt-get -y install cron && apt-get -y install pip
#Create the log file to be able to run tail
RUN touch /var/log/cron.log

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./Conjugat-django/requirements.txt /usr/app/requirements.txt
RUN pip install -r requirements.txt