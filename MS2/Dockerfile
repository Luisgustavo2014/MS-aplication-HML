FROM python:3.8
COPY . /app/
ENV HOST='10.0.0.25'
ENV HOST_DATABASE='10.5.0.11'
EXPOSE 7002
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python main.py