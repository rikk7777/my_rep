FROM python:3.11.1

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /Bookbot

COPY ./Bookbot /Bookbot/

CMD ['python', 'main.py']