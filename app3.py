import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_file_directory
app = Flask(__name__)
import os, uuid
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
    file = request.files.get('file')

    if not file:
        return "No file uploaded"

    if file.content_type == 'text/plain':
        return file.read().decode()

    elif file.content_type in ['application/vnd.ms-excel', 'text/csv']:
        df = pd.read_csv(file)
        return df.to_html()

    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        df = pd.read_excel(file)
        return df.to_html()

    else:
        return "Unsupported file type"

@app.route('/converet_csv_two', methods = ['POST'])
def convert_csv_two():
  file = request.files['file']
  df = pd.read_excel(file)
  if not os.path.exists('downloads'):
    os.makedirs('downloads')
  filename = f'{uuid.uuid()}.csv'
  df.to_csv(os.path.join('downloads.html', filename), index=False)
@app.route('/download/<filename>')
def download(filename):
  return send_file_directory('downloads', filename)
if __name__ == '__main__':
 app.run(host = '0.0.0.0',port =  5555, debug=True)