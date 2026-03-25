FROM ubuntu:24.04

RUN apt update -y && apt install -y python3

WORKDIR /app

COPY app.py .

CMD ["python3", "app.py"]