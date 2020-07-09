from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route('/')
def show_form():
  """Show currency conversion form"""
  return render_template('form.html')