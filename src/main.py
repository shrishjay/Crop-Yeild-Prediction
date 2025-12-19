from preprocessing import *
from feature_engineering import *
from model import *
import pandas as pd
import numpy as np

file_path = "/home/shrishjay/projects/Crop-Yeild-Prediction/data/crop_production.csv"
df = remove_std_0(file_path)
df = mostly_zeros(df)
# df = low_sample(df, 100)
df = rem_0_yeild(df)
df = transform(df)
model = training(df)
