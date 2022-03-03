FROM python:3.8-alpine
COPY ./API/requirements.txt /app/requirements.txt
COPY ./API/ /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN ls -l
#RUN python ./app/server.py
EXPOSE 7000
      