from flask import Flask, request, json, jsonify
from joblib import load
from PIL import Image
from io import BytesIO
import numpy as np


headers = {"Content-Type": "application/json; charset=utf-8"}

app = Flask(__name__)


@app.route("/")
def hello_world():    

    print(request.headers)

    print('------')

    print(request.headers.get('Authorization'))
    print(request.headers.get('Content-Type'))
    print(request.headers.get('Accept'))
    #return str(request.headers.get('Content-Type'))
    return "Hello Everyone."
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
    z = int(x) + int(y) 
    return {'sum':z}


@app.route("/testpost", methods=['POST'])
def test_post():
    #image1 = request.json['image1']
    #image2 = request.json['image2']
    print("done loading")
    
    return "Done Loading"

@app.route("/predict", methods=['POST'])
def predict_image():
    image1 = request.json['image1']
    #image2 = request.json['image2']
    print("done loading")
    model_path = "./models/svm_gamma0.01_C1.joblib"
    model = load(model_path)
    predicted1 = model.predict([image1])
    #predicted2 = model.predict([image2])
   
    # if predicted1 == predicted2 :
    #     result = True
    # else :
    #     result = False
    # #return {"y_predicted":int(predicted[0])}
    # return result
    #return "prediction"
    return {"y_predicted":int(predicted1[0])}

@app.route('/predict_digit', methods=['POST'])
def predict_digit():
    if 'image' not in request.files:
        return jsonify(error='Please provide an image.'), 400

    image_bytes = request.files['image'].read()
    image = Image.open(BytesIO(image_bytes)).convert('L')
    image = image.resize((8, 8), Image.LANCZOS)
    
    image_arr = np.array(image).reshape(1, -1)
    
    model_path = "./models/model.joblib"
    model = load(model_path)
    #model = joblib.load('model.joblib')

    pred = model.predict(image_arr)

    return jsonify(predicted_digit=int(pred[0]))


@app.route('/string_example', methods=['POST'])
def handle_non_json():
    content_type = request.headers.get('Content-type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
        return data
    else:
        return "Content type is not supported."
    

