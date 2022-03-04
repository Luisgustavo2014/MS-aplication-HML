FROM python:3.8-alpine
COPY ./API/requirements.txt /app/requirements.txt
COPY ./API/ /app/
ENV HOST='10.5.0.10'
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python server.py
EXPOSE 7000
      