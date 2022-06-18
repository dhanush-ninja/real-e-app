FROM python:3

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

LABEL maintainer='api.imperfect@gmail.com'
LABEL youtube="https://www.youtube.com/c/APIImperfect"
LABEL decription="Development image for Real Estate Project"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt update \
  && apt install -y build-essential \
  && apt install -y libpq-dev \
  && apt install -y gettext \
  && apt -y install netcat gcc postgresql \
  && apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt


RUN pip3 install -r requirements.txt

RUN pip3 install djangorestframework-simplejwt==5.2.0

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT [ "/entrypoint"]