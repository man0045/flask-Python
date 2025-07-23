import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')
@app.route('/', methods=['GET', 'POST'])
def methods():
 if request.method == 'GET':
  myval = 'myvalue'
  return render_template('index.html', myval = myval)
 elif request.method == 'POST':
  username = request.form.get('username')
  password = request.form.get('password')
  if(username == 'mannu' and password == 'pass'):
   return 'Success'
  else:
   return 'Failure'

@app.route('/file_upload', methods=['POST'])
def file_upload():
 return ""
if __name__ == '__main__':
 app.run(host = '0.0.0.0',port =  5555, debug=True)