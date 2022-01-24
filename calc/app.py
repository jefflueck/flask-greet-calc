# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def do_add():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))

  result = a + b
  return f"<h1>The result of {a} &#43 {b} is &#58; {result}</h1>"

@app.route('/sub')
def do_sub():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))

  result = b - a
  return f"<h1>The result of {b} &#8722; {a} is &#58; {result}</h1>"

@app.route('/mult')
def do_mult():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))

  result = a * b
  return f"<h1>The result of {a} &#215; {b} is &#58; {result}</h1>"


@app.route('/div')
def do_div():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))

  result = a / b
  return f"<h1>The result of {a} &divide {b} is &#58; {result}</h1>"
