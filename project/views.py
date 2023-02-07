from flask import Flask, render_template, request
import joblib
import pandas as pd 
import numpy as np



app = Flask(__name__)

app.app_context().push()

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', message='Get started')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

# import d'un petit fichier de users
def valid_login():
    with open('users.txt', 'r') as users:
        for i, j in users:
            users[i]
            users[j]

def log_user_in():
    return render_template('auth/dashboard.html')

@app.route('/auth/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # le code suivant est exécuté si la méthode 
    # fut GET ou les identifiants étaient incorrectes
    return render_template('auth/login.html')

@app.route('/auth/dashboard')
def dashboard():
    return render_template('auth/dashboard.html')

# Les fichiers doivent être placés à la racine du projet
# autrement ils sont introuvbales par Python !!!
mdl1 = 'NearestNeighbors.joblib'
mdl2 = 'LogisticRegression.joblib'

# Chargement du modèle
with open(mdl2, 'rb') as model:
    joblib.load(model)

@app.route('/auth/predict')
def predict():
    if request.method == 'POST':
        # Récupérer les données d'entrée à partir du corps de la requête
        data = request.form
        feature1 = data["feature1"]
        feature2 = data["feature2"]
        feature3 = data["feature3"]

        # Prédiction
        features = np.array([[feature1, feature2, feature3]])
        result = model.predict(features)

        return {"result" : result.tolist()}
    return render_template('auth/predict.html')
