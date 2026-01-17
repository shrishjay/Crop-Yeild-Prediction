import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle


file_path = "/home/shrishjay/projects/Crop_Yield_Prediction/ML_pipeline/data/crop_production.csv"
df = pd.read_csv(file_path)


def training(df):
    x = df.drop(["Yield_ton_per_hec"], axis=1)
    y = df["Yield_ton_per_hec"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.20, random_state=42
    )
    regressor = RandomForestRegressor(random_state=0, oob_score=True)
    print(x_train)
    print(x_test)
    model = regressor.fit(x_train, y_train)
    model_pkl_file = "/home/shrishjay/projects/Crop_Yield_Prediction/model/model.pkl"
    with open(model_pkl_file, "wb") as file:
        pickle.dump(model, file)
    print(model.score(x_test, y_test))
    return model
