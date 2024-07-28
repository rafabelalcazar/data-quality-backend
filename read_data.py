import pandas as pd

df = pd.read_csv('./datasets/output.csv', encoding='latin1')

print(df.head())