import numpy as np
from flask import Flask, jsonify, request, render_template
import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) if (x != "") else np.nan for x in request.form.values()]
    final_features = np.array(int_features)
    print(final_features)
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
