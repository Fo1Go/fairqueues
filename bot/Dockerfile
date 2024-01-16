FROM python:3.12.0
WORKDIR ./bot
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFED 1
COPY requirements.txt .
RUN ["pip", "install", "-r", "requirements.txt"]
COPY . .