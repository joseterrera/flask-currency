from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import currency

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
  
  if not errors:
    result = currency.convert_to_pretty(code_from, code_to, amt)
    if result is None:
      errors.append('Conversion Failed')


  if errors:
    for error in errors:
      flash(err)
    return render_template('form.html',
                            code_from=code_from,
                            code_to=code_to,
                            amt=amt or "") 
  else:
    return render_template('results.html', result=f"{result}") 
