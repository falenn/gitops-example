#!/bin/env python

from flask import Flask
from flask_healthz import healthz
from flask_healthz import HealthError

app = Flask(__name__)
app.register_blueprint(healthz, url_prefix="/healthz")

@app.route("/")
def hello():
  return "Hello out there!"

def liveness():
  pass

# readiness probe. - use to test connections to dbs, external dependencies, etc.
def readiness():
  try:
    True
  except Exception:
    raise HealthError("Can't perform function")


  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000)


