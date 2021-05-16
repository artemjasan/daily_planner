FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /daily_planner

COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .