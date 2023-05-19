FROM python:3.11-buster

LABEL maintainer="Pierre-Henri Bourdeau <phbasic@gmail.com>"

ARG USERNAME=app
ARG USER_UID=1000
ARG USER_GID=$USER_UID



# RUN groupadd --gid $USER_GID $USERNAME \
#     && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME --home-dir /app

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    build-essential \
    ; \
    rm -rf /var/lib/apt/lists/*


# USER app

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:app"]