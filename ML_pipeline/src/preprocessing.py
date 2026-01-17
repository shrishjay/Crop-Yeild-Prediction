import pandas as pd

file_path = "/home/shrishjay/projects/Crop_Yield_Prediction/ML_pipeline/data/crop_production.csv"
df = pd.read_csv(file_path)


def basic_clean(df):
    """Drop the unecessary columns"""
    df_clean = df.drop(columns=["Area_in_hectares", "Production_in_tons"])
    return df_clean


def rem_0_yeild(df):
    """Remove the rows which have 0 yeild per hectare"""
    zero_counts = (df["Yield_ton_per_hec"] == 0).sum()
    if zero_counts > 0:
        df = df[df["Yield_ton_per_hec"] > 0]
        return df
    else:
        return df


def mostly_zeros(df):
    """Removes the crops which majorly have 0 yeild values
    For this data it is cauliflower bottlegourd and bittergourd"""
    zero_crops = ["cauliflower", "bottlegourd", "bittergourd"]
    df = df[~df["Crop"].str.lower().isin(zero_crops)]
    return df


def rem_outlier(df):
    """Removes outliers for each crop yeild per hectare"""
    q1 = df.groupby("Crop")["Yield_ton_per_hec"].quantile(0.25)
    q3 = df.groupby("Crop")["Yield_ton_per_hec"].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df = df[
        (df["Yield_ton_per_hec"] >= df["Crop"].map(lower))
        & (df["Yield_ton_per_hec"] <= df["Crop"].map(upper))
    ]
    return df
