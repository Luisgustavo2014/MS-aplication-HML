FROM python:3.8-alpine
COPY ./API/requirements.txt /app/requirements.txt
COPY ./API/ /app/
ENV HOST='144.22.139.197'
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python server.py
EXPOSE 7000
