

from flask import Flask, request
from transformers import pipeline

app = Flask(__name__)
model = None


def load_model():
	global model 
	model_path = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
	model = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path) 


@app.route('/')
def home_endpoint():
	return "Hello World"


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample

    # data = request.json['data'] # Get data posted as a json
    data = request.json
    print(data)
    prediction = model(data)  # runs globally loaded model on the data
    return prediction

if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
