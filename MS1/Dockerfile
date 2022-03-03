FROM python:3.8-alpine
COPY ./MS1/ /app/requirements.txt
COPY ./MS1/ /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python ./rabbit_recive/revice_queue.py
#RUN ls -l
EXPOSE 7001