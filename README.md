# ML Model Deployment using Flask

## Overview

This repository contains the files to create a basic ML web app using Flask. The model used here is trained on the data provided in **"Tabular Playground Series - Jan 2021"** Kaggle competition. 

## Instructions

1. [This](https://www.kaggle.com/harshitt21/tabular-playground-series-script/output?scriptVersionId=53845237&select=submission.csv) is the script used to create the models that are to be deployed. As I was using 5 Fold CV, there are 5 different models, whose predictions are averaged to get the final prediction. 

2. In **app.py**, I am only using a single model as loading all the models into the memory at once was raising Heroku memory errors. 

3. The goal of creating this ML app was just to try deploying ML models. I used Flask as it is easy to learn. Will be trying Streamlit after this.  

4. I've deployed this on [Heroku](https://ml-app-deploy-flask.herokuapp.com/), but sometimes it crashes due to memory overloading, you can recreate this on your PC by cloning this repo and downloading models from the link mentioned in Intruction 1 and then running:
    ```
    pip install -r requirements.txt
    python app.py
    ```
    
