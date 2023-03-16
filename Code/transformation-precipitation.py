import pandas as pd
import numpy as np
import re

## Muatkan file CSV ke dalam bingkai data Pandas (Load the CSV file into a Pandas)
df = pd.read_csv('/Users/Bowen/Downloads/Final_Project/source_data/sample-data/USW00023169-LAS_VEGAS_MCCARRAN_INTL_AP-precipitation-inch.csv')

## Bersihkan kolom presipitasi (Clean the precipitation column)
df['precipitation'] = pd.to_numeric(df['precipitation'], errors='coerce')
df['precipitation'] = df['precipitation'].replace(0.0, None)
df['precipitation'] = df['precipitation'].replace('', None)

## Menghilangkan baris dengan nilai kosong (Drop rows with empty values)
df.dropna(inplace=True)

## Simpan bingkai data yang telah dibersihkan ke file CSV baru (Save the cleaned dataframe to a new CSV file)
df.to_csv('/Users/Bowen/Downloads/Final_Project/data_transformation/transformation-precipitation-LasVegas.csv', index=False)

print('Data cleansing success')
