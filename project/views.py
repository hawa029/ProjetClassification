from flask import Flask, render_template

app = Flask(__name__)

app.app_context().push()

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', message='Get started')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/auth/login')
def login():
    return render_template('auth/login.html')

@app.route('/auth/dashboard')
def dashbooard():
    return render_template('auth/dashboard.html')

@app.route('/auth/predict')
def predict():
    return render_template('auth/predict.html')
