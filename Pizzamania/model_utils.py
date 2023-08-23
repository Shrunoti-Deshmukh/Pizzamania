import pickle
import pandas as pd
import xgboost as xgb


def load_model():
    model = xgb.Booster()
    model.load_model('C:/Users/HP/Downloads/pizza_model.xgb')
    return model

def make_prediction(model, data):
    data_matrix = xgb.DMatrix(data)
    prediction = model.predict(data_matrix)
    return prediction[0]