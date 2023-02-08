from flask import Flask, render_template, request
import pickle
from sklearn.tree import DecisionTreeClassifier
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
mdl1 = 'DecisionTree.pkl'
mdl2 = 'LogisticRegression.pkl'

# On charge le modèle
with open(mdl1, 'rb') as model:
    model = pickle.load(model)

@app.route('/auth/predict', methods=['POST'])
def predict_post():
    feature1 = int(request.form["feature1"])
    #feature2 = float(request.form["feature2"])
    #feature3 = (request.form["feature3"])

    # Prédiction
    prediction = model.predict(np.array([[feature1, 0]]))

    return render_template('auth/prediction.html', prediction=prediction)

@app.route('/auth/prediction')
def predict():
    return render_template('auth/predict.html')
