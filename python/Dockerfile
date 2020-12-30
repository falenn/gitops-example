FROM python:3-alpine
LABEL author="falenn" version="1.0" github_repo="https//github.com/falenn/gitops-example"
COPY ./webapp /python/webapp
WORKDIR /python/webapp
RUN pip install -r /python/webapp/requirements.txt
ENV FLASK_CONFIG=/python/webapp/defaults.cfg
ENV FLASK_APP=/python/webapp
EXPOSE 5000
ENTRYPOINT ["flask", "run","--host=0.0.0.0"]

