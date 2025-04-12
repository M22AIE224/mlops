from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/sum/<x>/<y>")
def sum_num(x,y):
    sum = int(x) + int(y)
    retunr(str(sum)) 


@app.route("/model" , methods = ['POST'])
def pred_model():
    js = request.get_json()
    x=js['x']
    y=js['y']
    return x+y