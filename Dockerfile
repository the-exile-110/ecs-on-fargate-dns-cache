FROM python:3.8-slim-buster

WORKDIR /app
ADD . /app

COPY ./dnsmasq.conf /etc/dnsmasq.conf

RUN apt-get update && apt-get install -y dnsutils dnsmasq

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["./start.sh"]