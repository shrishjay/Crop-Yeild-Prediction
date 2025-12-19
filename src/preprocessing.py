import pandas as pd


def remove_std_0(file_path):
    """Groups all the crops by their names
    and removes the rows which have std of their yeild per hectare value 0"""
    df = pd.read_csv(file_path)
    std_count = df.groupby("Crop")["Yield_ton_per_hec"].std()
    std_zero = std_count[std_count == 0].index.tolist()
    df_clean = df[~df["Crop"].isin(std_zero)].copy()
    return df_clean


def mostly_zeros(df):
    """Removes the crops which majorly have 0 yeild values
    For this data it is cauliflower bottlegourd and bittergourd"""
    zero_crops = ["cauliflower", "bottlegourd", "bittergourd"]
    df = df[~df["Crop"].str.lower().isin(zero_crops)]
    return df


# def low_sample(df, size):
#     low_crops = df["Crop"].value_counts() < size.index.tolist()
#     return low_crops


def rem_0_yeild(df):
    """Remove the rows which have 0 yeild per hectare"""
    zero_counts = (df["Yield_ton_per_hec"] == 0).sum()
    if zero_counts > 0:
        df = df[df["Yield_ton_per_hec"] > 0]
        return df
    else:
        return df
