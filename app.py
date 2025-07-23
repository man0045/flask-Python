import requests
from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/')
def hello_world():
 return '<h1>Hello, World!<h1/>'
@app.route('/greet/<name>')
def greet(name):
 return f"Hello {name}"

@app.route('/hello', methods = ['POST', 'GET'])
def hello():
 if request.method == 'POST':
  return 'Hello, POST request'
 elif request.method == 'GET':
  return 'Hello, GET request'
 else: 
  return 'Hello for reason' 

@app.route('/handle_url_params')
def handle_params():
 if 'greeting' in request.args.keys() and 'name' in request.args.keys():
  greeting = request.args['greeting']
  name = request.args.get['name']
  return f"{greeting}, {name}"
 else:
  return "Missing required parameters"

@app.route('/hello2')
def hello2():
 response = make_response('hello\n')
 response.status_code = 202
 response.headers['Content-Type'] = 'application/octet-stream'
 return response

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
 return f"sum of {number1} and {number2} is {number1 + number2}"
if __name__ == '__main__':
 app.run(host = '0.0.0.0',port =  5555, debug=True)