from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
# definition de la page d'accueil
def home():
    return render_template('index.html')

@app.route('/login')
# definition de la page de login
def login():
    return render_template('login.html')

@app.route('/dashboard')
# definition de la page dashboard
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict')
# definition de la page de badges
def predict():
    return render_template('predict.html')

@app.route('/contact')
# definition de la page collapsible
def contact():
    return render_template('contact.html')





if __name__ == '__main__':
    app.run(debug=True)
