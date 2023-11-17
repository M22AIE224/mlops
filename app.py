from flask import Flask, request, json
from joblib import load

headers = {"Content-Type": "application/json; charset=utf-8"}

app = Flask(__name__)
#model_path = "models/svm_gamma0.01_C1.joblib"
#model = load(model_path)


@app.route("/")
def hello_world():
    

    print(request.headers)

    print('------')

    print(request.headers.get('Authorization'))
    print(request.headers.get('Content-Type'))
    print(request.headers.get('Accept'))
    return str(request.headers.get('Content-Type'))
    #return "<p>Home: bobbyhadz.com</p>"

@app.route("/sum/<x>/<y>")
def sum_num(x,y):
    sum = int(x) + int(y)
    return(str(sum)) 



@app.route('/model' , methods = ['POST'])
def pred_model():
    #print(request.headers)

    #print('------')

    #print(request.headers.get('Authorization'))
    #print(request.headers.get('Content-Type'))
    #print(request.headers.get('Accept'))
    x = request.json['x']
    y = request.json['y']
    z = x + y 
    return {'sum':z}


@app.route("/predict" , methods = ['POST'])
def pred_compare():
    js = request.get_json()
    x=js['x']
    y=js['y']
    return x+y


@app.route('/string_example', methods=['POST'])
def handle_non_json():
    content_type = request.headers.get('Content-type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
        return data
    else:
        return "Content type is not supported."
    

