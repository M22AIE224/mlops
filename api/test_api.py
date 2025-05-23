from app import app
import pytest
import json
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
# from prediction import predict_digit
import joblib
import os
from PIL import Image
from io import BytesIO

def get_sample_data(image):
    pil_image = Image.fromarray(image.astype('uint8'))
    img_byte_arr = BytesIO()
    pil_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

#added test case for flask call

def test_post_predict():
    digits = datasets.load_digits()
    X, y = digits.images, digits.target

    for digit in range(10):
        print(f"----[executing]: {digit}")
        index = next(i for i, label in enumerate(y) if label == digit)
        image_bytes = get_sample_data(X[index])

        response = app.test_client().post(
            '/predict_digit', 
            data={'image': (BytesIO(image_bytes), 'image.png')},
            content_type='multipart/form-data'
        )

        assert response.status_code == 200
        print(f"----Status Code : {response.status_code}")
        assert response.get_json()['predicted_digit'] == digit
        print(f"----Digit : {digit}")

