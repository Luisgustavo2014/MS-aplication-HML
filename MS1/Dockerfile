FROM python:3.8-alpine
COPY . /app/
ENV HOST='10.0.0.57'
ENV HOST_DATABASE='10.5.0.11'
EXPOSE 7001
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python rabbit_recive/revice_queue.py