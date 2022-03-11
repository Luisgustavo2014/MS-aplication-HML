FROM python:3.8-alpine
COPY . /app/
ENV HOST='10.0.0.34'
EXPOSE 7000
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python server.py

