from flask import Flask, render_template
app = Flask(__name__, template_folder= 'templates')
@app.route('/')
def index():
 myval = 'myvalue'
 num = 10+20
 mylist = [1, 2, 3, 4, 5]
 return render_template('index.html', myval = myval, num = num, mylist = mylist)

if __name__ == '__main__':
 app.run(host ='0.0.0.0', debug=True)