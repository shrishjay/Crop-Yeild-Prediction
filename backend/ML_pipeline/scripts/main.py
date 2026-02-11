from preprocessing import *
from feature_engineering import fit_encode
from model import training
import pandas as pd
import numpy as np

file_path = "/home/shrishjay/projects/Crop_Yield_Prediction/backend/ML_pipeline/data/crop_production.csv"
df = pd.read_csv(file_path)
df = basic_clean(df)
df = rem_0_yeild(df)
df = mostly_zeros(df)
df = rem_outlier(df)
df = fit_encode(df)
model = training(df)
