from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)

app.app_context().push()

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', message='Get started')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')


@app.route('/auth/login', methods=['POST', 'GET'])
def login():
    return render_template('auth/login.html')

@app.route('/auth/dashboard')
def dashboard():
    return render_template('auth/dashboard.html')

# Les fichiers doivent être placés à la racine du projet
# autrement ils sont introuvbales par Python !!!
mdl1 = 'DecisionTree.pkl'
mdl2 = 'LogisticRegression.pkl'
mdl3 = 'model_adaBoost.pkl'

# On charge le modèle
with open(mdl2, 'rb') as model:
    model = pickle.load(model)

@app.route('/auth/predict', methods=['POST'])
def predict_post():
    feature1 = int(request.form["feature1"])
    #feature2 = float(request.form["feature2"])
    #feature3 = (request.form["feature3"])

    # Prédiction sur une donnée
    x = np.array([[feature1], [0]])
    model.predict(x)

    good = 'cette transaction n\'est pas une fraude'
    bad = 'Cette transaction est une fraude'

    prediction = [good, bad]
    if x[0] == 0:
        
        prediction = prediction[0]
    else:
        prediction = prediction[1]

    return render_template('auth/prediction.html', prediction=prediction)

@app.route('/auth/prediction')
def predict():
    return render_template('auth/predict.html')
