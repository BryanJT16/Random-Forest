import pickle
import numpy as np
import json
import os

# CARGAR EL MODELO =====
with open("models/gradientboost_model.sav", "rb") as archivo:
    modelo  = pickle.load(archivo)

print("Modelo cargado.")

columnas = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]


# EJEMPLOS DE ENTRADA LEGIBLE =====
ejemplos = [
    {
        "Pregnancies": 2,
        "Glucose": 95,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 85,
        "BMI": 24.5,
        "DiabetesPedigreeFunction": 0.351,
        "Age": 31,
    },
    {
        "Pregnancies": 1,
        "Glucose": 110,
        "BloodPressure": 80,
        "SkinThickness": 25,
        "Insulin": 0,
        "BMI": 28.2,
        "DiabetesPedigreeFunction": 0.248,
        "Age": 45,
    }
]

# PREDICCIÓN =====
X = np.array([
    [e[col] for col in columnas]
    for e in ejemplos
])

prediccion = modelo.predict(X)

for i, pred in enumerate(prediccion):
    estado = "Tiene diabetes" if pred == 1 else "No tiene diabetes"
    print(f"Ejemplo {i+1}: {estado}")