import pandas as pd
import numpy as np
import re

## Muatkan file CSV ke dalam bingkai data Pandas (Load the CSV file into a Pandas)
df = pd.read_csv('/Users/Bowen/Downloads/Final_Project/source_data/sample-data/USW00023169-temperature-degreeF.csv')

## Bersihkan kolom min (Clean the min column)
df['min'] = pd.to_numeric(df['min'], errors='coerce')
df['min'] = df['min'].replace('', None)

## Bersihkan kolom maks (Clean the max column)
df['max'] = pd.to_numeric(df['max'], errors='coerce')
df['max'] = df['max'].replace('', None)

## Bersihkan kolom normal_min (Clean the normal_min column)
df['normal_min'] = pd.to_numeric(df['normal_min'], errors='coerce')
df['normal_min'] = df['normal_min'].replace('', None)

## Bersihkan kolom normal_max (Clean the normal_max column)
df['normal_max'] = pd.to_numeric(df['normal_max'], errors='coerce')
df['normal_max'] = df['normal_max'].replace('', None)

## Menghilangkan baris dengan nilai kosong (Drop rows with empty values)
df.dropna(inplace=True)

## Simpan bingkai data yang telah dibersihkan ke file CSV baru (Save the cleaned dataframe to a new CSV file)
df.to_csv('/Users/Bowen/Downloads/Final_Project/data_transformation/transformation-temperature-LasVegas.csv', index=False)

print('Data cleansing success')
