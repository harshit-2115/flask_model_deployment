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
    final_features = np.array(int_features).reshape((1, -1))
    model1 = joblib.load('./results/LGBmodel_1.pkl')
    # model2 = joblib.load('./results/LGBmodel_2.pkl')
    # model3 = joblib.load('./results/LGBmodel_3.pkl')
    # model4 = joblib.load('./results/LGBmodel_4.pkl')
    # model5 = joblib.load('./results/LGBmodel_5.pkl')
    pred1 = model1.predict(final_features)
    # pred2 = model2.predict(final_features)
    # pred3 = model3.predict(final_features)
    # pred4 = model4.predict(final_features)
    # pred5 = model5.predict(final_features)
    # final_prediction = (pred1+pred2+pred3+pred4+pred5)/5
    return render_template('index.html', predicted_value=f'Predicted Value is {float(pred1)}')
    
    


if __name__ == "__main__":
    app.run(debug=True)
