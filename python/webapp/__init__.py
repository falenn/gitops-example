from flask import Flask
from flask_healthz import healthz
from prometheus_flask_exporter import PrometheusMetrics
import os


app = Flask(__name__, static_url_path='/static')
app.register_blueprint(healthz, url_prefix="/healthz")
app.config.from_envvar("FLASK_CONFIG")

metrics = PrometheusMetrics(app)
# static information as metric
VERSION = os.environ['FLASK_APP_VERSION']
metrics.info('app_info', 'Application info', version=VERSION)

import webapp.views
import webapp.checks

