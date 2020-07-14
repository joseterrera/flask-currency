from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import currency

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


def safe_convert_to_float(s):
  """Convert to float or return none
  >>> safe_convert_to_float("1.2")
  1.2
  >>> safe_convert_to_float("hello") is None
  True
  """
  try:
    return float(s)
  except ValueError:
    return None


@app.route('/')
def show_form():
  """Show currency conversion form"""
  return render_template('form.html')

@app.route('/convert')
def submit_form():
  """Handle Form Submission"""
  code_from = request.args['code_from'].upper()
  code_to = request.args['code_to'].upper()
  # amt = safe_convert_to_float(request.args['amt'])
  amt = safe_convert_to_float(request.args['amt'])
  errors = []

  if amt is None:
        errs.append("Not a valid amount.")


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
    return render_template('result.html', result=f"{result}") 
