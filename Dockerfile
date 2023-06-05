FROM python:3

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./django_project /app

WORKDIR /app

COPY ./entrypoint.sh .
ENTRYPOINT ["bash", "./entrypoint.sh"]
