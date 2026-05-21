# Python 3.12 LTS — se actualizará a 3.14 cuando salga versión estable
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
