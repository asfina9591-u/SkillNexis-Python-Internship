# Use Pandas to load and analyze CSV
import pandas as pd

df = pd.read_csv("students.csv")
print("Head:\n", df.head())
print("Summary:\n", df.describe())
