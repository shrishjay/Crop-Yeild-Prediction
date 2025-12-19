import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.use("TkAgg")

df = pd.read_csv("/home/shrishjay/projects/Crop-Yeild-Prediction/data/crop_yield.csv")
pd.set_option("display.max_columns", None)
print(df.head())
sns.distplot(df["Yield_tons_per_hectare"])
plt.show()
