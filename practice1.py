import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\PYTHON PRACTICE\Lab Assignment 14B\gold_karat.csv")
print(df.head())

plt.scatter(df['karat'], df['Sell Price($)'])
