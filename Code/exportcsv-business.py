import json

def export_to_csv():
    file_path = '/Users/Bowen/Downloads/Final_Project/data_transformation/yelp-dataset/yelp_academic_dataset_business.json'
    with open(file_path) as f:
        list1 = []
        data = [json.loads(line) for line in f] 
        temp = data[0]
        header_items = []
        get_header_items(header_items, temp)
        list1.append(header_items)
        print(list1)

def get_header_items(items, obj):
    for x in obj.keys():
        if isinstance(obj[x], dict):
            items.append(x)
            get_header_items(items, obj[x])
        else:
            items.append(x)


export_to_csv()
