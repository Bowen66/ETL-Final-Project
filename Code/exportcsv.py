import json
import csv

## Open the JSON file and load the data (Buka file JSON dan muat data)
with open('/Users/Bowen/Downloads/Final_Project/data_transformation/yelp-dataset/yelp_academic_dataset_business.json', 'r') as f:

    ## Iterate through each line in the file (Lakukan perulangan pada setiap baris dalam file)
    for line in f:
        ## Load the line as a JSON object
        data = json.loads(line)
        
        ## Get the column names
        headers = list(data.keys())
        
        ## Iterate through each column name (Lakukan iterasi melalui setiap nama kolom)
        for header in headers:
            ## If the column name is "attributes" (Jika nama kolomnya adalah "atribut")
            if header == "attributes":
                ## Get the subheaders of the "attributes" column (Dapatkan subpos dari kolom "atribut")
                subheaders = list(data[header].keys())
                
                ## Print out the subheaders
                print(subheaders)


