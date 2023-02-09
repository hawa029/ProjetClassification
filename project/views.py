from flask import Flask, render_template, session, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd
from .models import db, User

app = Flask(__name__)

app.app_context().push()

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', message='Commencez !')

@app.route('/auth/register')
# fonction qui enregistre un nouvel utilisateur
def register():
    # récupération des données du formulaire
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        db.create_all()

        return redirect(url_for('/index'))

    return render_template('auth/register.html')


@app.route('/auth/login', methods=['POST', 'GET'])
def login():
    # 
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    return render_template('auth/login.html')

@app.route('/auth/dashboard')
def dashboard():
    return render_template('auth/dashboard.html')

# Les fichiers doivent être placés à la racine du projet
# autrement ils sont introuvbales par Python !!!
mdl1 = 'DecisionTree.pkl'
mdl2 = 'LogisticRegression.pkl'
mdl3 = 'model_adaBoost.pkl'# Ce modèle requiert 8 features

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
