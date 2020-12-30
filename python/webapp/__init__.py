#!/bin/env python

from flask import Flask
from flask_healthz import healthz

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(healthz, url_prefix="/healthz")
app.config.from_envvar("FLASK_CONFIG")


import webapp.views
import webapp.checks

