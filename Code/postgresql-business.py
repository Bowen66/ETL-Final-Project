import pandas as pd
import psycopg2
import csv
import os
from dotenv import load_dotenv

# def configuration files
load_dotenv()
host = os.getenv('pg_host')
port = os.getenv('pg_port')
dbname = os.getenv('pg_dbname')
user = os.getenv('pg_user')
password = os.getenv('pg_pass')

# connect to postgresql
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
    CREATE TABLE IF NOT EXISTS business_yelp (
        business_id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255),
        city VARCHAR(255),
        state VARCHAR(255),
        postal_code VARCHAR(255),
        latitude FLOAT,
        longitude FLOAT,
        stars FLOAT,
        review_count INT,
        is_open INT,
        attributes VARCHAR(255),
        categories VARCHAR(255),
        hours VARCHAR(255)
    )
"""
## Jalankan kueri untuk membuat tabel (Execute the query to create the table)
cur.execute(create_table_sql)

## Tentukan jalur dan nama file file CSV (Specify the path and filename of the CSV file)
csv_path = '/Users/Bowen/Downloads/Final_Project/data_transformation/business.csv'

## Buka file CSV dan masukkan isinya ke dalam database (Open the CSV file and insert its contents into the database)
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    ## Lewati baris header (skip the header row)
    next(csv_reader)

    ## Ulangi setiap baris dalam file CSV dan masukkan ke dalam database (Loop through each row in the CSV file and insert it into the database)
    for row in csv_reader:
        business_id = row[0]
        name = row[1]
        address = row[2]
        city = row[3]
        state = row[4]
        postal_code = row[5]
        latitude = float(row[6])
        longitude = float(row[7])
        stars = float(row[8])
        review_count = int(row[9])
        is_open = int(row[10])
        attributes = row[11]
        categories = row[12]
        hours = row[13]

        ## Menentukan kueri SQL untuk menyisipkan baris ke dalam database (Define the SQL query to insert a row into the database) 
        sql = """
            INSERT INTO business_yelp (business_id, name, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open, attributes, categories, hours)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
## Jalankan kueri (Execute the query)
cur.execute(sql, (business_id, name, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open, attributes, categories, hours))

## Menyimpan perubahan ke basis data (Commit the changes to the database)
conn.commit()

## Menutup koneksi database (Close the database connection)
cur.close()
conn.close()

print('Database insertion success')