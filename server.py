from flask import Flask, request, url_for,render_template, jsonify
from transformers import pipeline

app = Flask(__name__)
model = None

def load_model():
	global model 
	model_path = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
	model = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path) 

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Works only for a single sample
    data = request.json
    prediction = model(data)  # runs globally loaded model on the data
    return jsonify(prediction[0])

@app.route('/predict', methods=['POST'])
def predict():
    # Works only for a single sample
    data = request.form.get('text for sentimental analysis')
    prediction = model(data)  # runs globally loaded model on the data
    return render_template("home.html", prediction_text=prediction)

if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
