from flask import Flask
import pandas as pd
import pickle
import random

loaded_model = pickle.load(open('app/model/model.sav', 'rb'))


@app.route('/')
def func():
    return "Home"


@app.route('/singlePred', methods=['POST'])
def SinglePrediction():
    df = pd.read_csv('dataset.csv')
    sample = df.sample()
    result = loaded_model.predict(sample)
    return result


@app.route("/batchPred",  methods=['POST'])
def BatchPrediction():
    df = pd.read_csv('dataset.csv')
    predictions = []
    for i in len(df):
        row = df.iloc[i]
        row = row.to_numpy()
        result = loaded_model.predict(row)
        predictions.append(result)
    for prediction in predictions:
        print(prediction)
    return 'predictions above'
