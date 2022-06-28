FROM python:3.8-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

COPY . .