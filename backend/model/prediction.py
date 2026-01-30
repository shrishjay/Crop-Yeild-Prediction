import pickle
import pandas as pd
from ML_pipeline.src.feature_engineering import transform

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


def predict(input_df):
    df = pd.DataFrame([input_df])
    df_clean = transform(df, encoder)
    df_final = df_clean[model.feature_names_in_]
    pred = model.predict(df_final)[0]
    return pred
