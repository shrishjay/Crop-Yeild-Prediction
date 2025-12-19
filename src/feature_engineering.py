import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


def transform(df):
    df = df.copy()

    # NPK features
    df["npk_sum"] = df["N"] + df["P"] + df["K"]
    df["n_to_p_ratio"] = df["N"] / (df["P"] + 1)
    df["n_to_k_ratio"] = df["N"] / (df["K"] + 1)
    df["p_to_k_ratio"] = df["P"] / (df["K"] + 1)
    df["n_deficient"] = (df["N"] < 40).astype(int)
    df["p_deficient"] = (df["P"] < 20).astype(int)
    df["k_deficient"] = (df["K"] < 20).astype(int)

    # pH features
    df["ph_optimal"] = ((df["pH"] >= 6.0) & (df["pH"] <= 7.5)).astype(int)
    df["ph_distance"] = abs(df["pH"] - 6.5)
    df["ph_squared"] = df["pH"] ** 2

    # Climate features
    df["rainfall_temp"] = df["rainfall"] * df["temperature"]
    df["water_stress"] = df["temperature"] / (df["rainfall"] + 1)
    df = pd.get_dummies(df, columns=["Crop", "Crop_Type", "State_Name"])
    return df


def encode(df):
    encoder = OneHotEncoder(sparse_output=False)
    x = df[["Crop", "Crop_Type", "State_Name"]]
    encoded_array = encoder.fit_transform(x)
    features = encoder.get_feature_names_out(["Crop", "Crop_Type", "State_Name"])
    encoded_df = pd.DataFrame(encoded_array, columns=features, index=df.index)
    df_dropped = df.drop(["Crop", "Crop_Type", "State_Name"], axis=1)
    df_final = pd.concat([df_dropped, encoded_df], axis=1)
    return df_final
