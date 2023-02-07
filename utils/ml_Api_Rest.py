from flask import Flask, request
import numpy as np
import pickle

app = Flask(__name__)

# Charger le modèle entraîné
model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    # Récupérer les données d'entrée à partir du corps de la requête
    data = request.get_json()
    feature1 = data["feature1"]
    feature2 = data["feature2"]
    feature3 = data["feature3"]

    # Prédiction
    features = np.array([[feature1, feature2, feature3]])
    result = model.predict(features)

    return {"result": result.tolist()}

if __name__ == "__main__":
    app.run(debug=True)


'''
Dans ce code, création d'une application Flask exposant une seule route /predict 
et utilisant le protocole HTTP POST. 
La route /predict prend les données d'entrée en format JSON à partir du corps de la requête et 
les utilise pour effectuer la prédiction  avec le modèle de machine learning enregistré sur PC.
Les résultats de la prédiction sont ensuite renvoyés au client en format JSON. 
Cette application peut être utilisée comme API REST pour la prédiction de machine learning.
'''