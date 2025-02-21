import numpy as np
from flask import Flask, request, render_template
import pickle

from pyexpat import features

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])

    input_features = np.array([[area, bedrooms, bathrooms, stories]])
    prediction = model.predict(input_features)[0]  # Extract the first value

    return render_template("index.html", prediction_text="Estimated Price : $ {:.2f}".format(prediction))


if __name__ == "__main__":
    app.run(debug = True)