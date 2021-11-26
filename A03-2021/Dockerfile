# syntax=docker/dockerfile:1
FROM python:3.9.4-alpine3.13

COPY requirements.txt requirements.txt
RUN apk add build-base
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]

EXPOSE 80