from flask import Flask, render_template
app = Flask(__name__, template_folder= 'templates')
@app.route('/')
def index():
 myval = 'myvalue'
 num = 10+20
 mylist = [1, 2, 3, 4, 5]
 return render_template('index.html', myval = myval, num = num, mylist = mylist)

@app.route('/other')
def other():
 myval = 'myvalue'
 return render_template('other.html', myval = myval)

@app.template_filter('reverse_string')
def reverse_string(s):
 return s[::-1]

@app.template_filter('repeat')
def repeat(s):
 return s * 3
@app.template_filter('alternate')
def alternate(s):
 return ''.join([c.upper() if i%2==0 else c.lower() for i, c in enumerate(s)])
if __name__ == '__main__':
 app.run(host ='0.0.0.0', debug=True)