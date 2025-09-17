FROM python:3.10-slim-bookworm

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "app/main.py"]