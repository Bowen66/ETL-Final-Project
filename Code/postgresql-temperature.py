import pandas as pd
import psycopg2
import csv
import os
from dotenv import load_dotenv

## def configuration files
load_dotenv()
host = os.getenv('pg_host')
port = os.getenv('pg_port')
dbname = os.getenv('pg_dbname')
user = os.getenv('pg_user')
password = os.getenv('pg_pass')

## connect to postgresql
try:
    conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
            )
    
    print('Database connection success')
except:
    print('Database connection error')

## Buka kursor untuk melakukan operasi basis data (Open a cursor to perform database operations)
cur = conn.cursor()

## Tentukan kueri SQL untuk membuat tabel jika tidak ada (Define the SQL query to create the table if it does not exist)
create_table_sql = """
    CREATE TABLE IF NOT EXISTS temperature_lasvegas (
        date DATE PRIMARY KEY,
        min DECIMAL(5, 2),
        max DECIMAL(5, 2),
        normal_min DECIMAL(5, 2),
        normal_max DECIMAL(5, 2)
    )
"""
## Jalankan kueri untuk membuat tabel (Execute the query to create the table)
cur.execute(create_table_sql)

## Tentukan jalur dan nama file file CSV (Specify the path and filename of the CSV file)
csv_path = '/Users/Bowen/Downloads/Final_Project/data_transformation/transformation-temperature-LasVegas.csv'

## Buka file CSV dan masukkan isinya ke dalam database (Open the CSV file and insert its contents into the database)
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    ## Lewati baris header (skip the header row)
    next(csv_reader)

    ## Ulangi setiap baris dalam file CSV dan masukkan ke dalam database (Loop through each row in the CSV file and insert it into the database)
    for row in csv_reader:
        date = row[0]
        min = row[1]
        max = row[2]
        normal_min = row[3]
        normal_max = row[4]

        ## Menentukan kueri SQL untuk menyisipkan baris ke dalam database (Define the SQL query to insert a row into the database)
        sql = """
            INSERT INTO temperature_lasvegas (date, min, max, normal_min, normal_max)
            VALUES (%s, %s, %s, %s, %s)
        """

        ## Jalankan kueri (Execute the query)
        cur.execute(sql, (date, min, max, normal_min, normal_max))

## Menyimpan perubahan ke basis data (Commit the changes to the database)
conn.commit()

## Menutup koneksi database (Close the database connection)
cur.close()
conn.close()

print('Database insertion success')