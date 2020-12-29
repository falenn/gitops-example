FROM python:3-alpine

COPY . /python
WORKDIR /python
RUN pip install -r requirements.txt
ENV FLASK_CONFIG=/python/default.cfg
CMD python /python/app.py
