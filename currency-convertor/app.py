from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route('/')
def show_form():
  """Show currency conversion form"""
  return render_template('form.html')

@app.route('/conversion')
def submit_form():
  """Handle Form Submission"""
  code_from = request.args['code_from'].upper()
  code_to = request.args['code_to'].upper()
  amt = safe_convert_to_float(request.args['amt'])
  errors = []

  if amt is None:
    errors.append("Not a valid amount.")


  if not currency.check_currency_code(code_from):
    errors.append(f"Not a valid code: {code_from}")

  if not currency.check_currency_code(code_to):
    errors.append(f"Not a valid code: {code_to}")

  
