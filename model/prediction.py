import pickle
import pandas as pd
from ML_pipeline.src.feature_engineering import transform

with open("/home/shrishjay/projects/Crop_Yield_Prediction/model/model.pkl", "rb") as f:
    model = pickle.load(f)


def predict(input_df):
    df = pd.DataFrame([input_df])
    df_clean = transform(df)
    df_final = df_clean[model.feature_names_in_]
    pred = model.predict(df_final)[0]
    return pred
