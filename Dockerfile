FROM ubuntu:latest
LABEL authors="sharofiddin"

RUN apt-get update && \
    sudo install python3.11 && \
    sudo install pip3

WORKDIR /apps/python_django
COPY . /apps/python_django

RUN pip3 freeze install requarements.txt
COM [*]


ENTRYPOINT ["top", "-b"]