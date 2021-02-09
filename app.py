import numpy as np
from flask import Flask, jsonify, request, render_template
import joblib
import lightgbm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) if (x != "") else np.nan for x in request.form.values()]
    final_features = np.array(int_features).reshape((1, -1))
    model = joblib.load('./model.pkl')
    pred = model.predict(final_features)
    
    return render_template('index.html', predicted_value=f'Predicted Value is {float(pred)}')
    
if __name__ == "__main__":
    app.run(debug=True)
