from flask import render_template
from webapp import app

@app.route("/")
def root():
  return render_template('index.html') 
