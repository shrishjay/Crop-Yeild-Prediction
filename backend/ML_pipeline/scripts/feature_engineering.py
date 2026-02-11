import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle


def fit_encode(df):
    encoder = OneHotEncoder(sparse_output=False)
    x = df[["Crop", "Crop_Type", "State_Name"]]
    encoded_array = encoder.fit_transform(x)
    features = encoder.get_feature_names_out(["Crop", "Crop_Type", "State_Name"])
    encoded_df = pd.DataFrame(encoded_array, columns=features, index=df.index)
    df_dropped = df.drop(["Crop", "Crop_Type", "State_Name"], axis=1)
    df_final = pd.concat([df_dropped, encoded_df], axis=1)
    with open("../../model/encoder.pkl", "wb") as f:
        pickle.dump(encoder, f)
    return df_final


def transform(df, encoder):
    x = df[["Crop", "Crop_Type", "State_Name"]]
    encoded_array = encoder.transform(x)
    features = encoder.get_feature_names_out(["Crop", "Crop_Type", "State_Name"])
    encoded_df = pd.DataFrame(encoded_array, columns=features, index=df.index)
    df_dropped = df.drop(["Crop", "Crop_Type", "State_Name"], axis=1)
    df_final = pd.concat([df_dropped, encoded_df], axis=1)
    return df_final
