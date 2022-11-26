
# import csv
# import json
 
 
# # Function to convert a CSV to JSON
# # Takes the file paths as arguments
# def make_json(csvFilePath, jsonFilePath):
     
#     # create a dictionary
#     data = {}
     
#     # Open a csv reader called DictReader
#     with open(csvFilePath, encoding='utf-8') as csvf:
#         csvReader = csv.DictReader(csvf)
         
#         # Convert each row into a dictionary
#         # and add it to data
#         for rows in csvReader:
             
#             # Assuming a column named 'No' to
#             # be the primary key
#             key = rows['No']
#             data[key] = rows
 
#     # Open a json writer, and use the json.dumps()
#     # function to dump data
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#         jsonf.write(json.dumps(data, indent=4))
         
# # Driver Code
 
# # Decide the two file paths according to your
# # computer system
# csvFilePath = r'first_edit.csv'
# jsonFilePath = r'data.json'
 
# # Call the make_json function
# make_json(csvFilePath, jsonFilePath)

# import csv
# import json

# file = 'first_edit.csv'
# json_file = 'output_data.json'

# #Read CSV File
# def read_CSV(file, json_file):
#     csv_rows = []
#     with open(file) as csvfile:
#         reader = csv.DictReader(csvfile)
#         field = reader.fieldnames
#         for row in reader:
#             csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
#         convert_write_json(csv_rows, json_file)

# #Convert csv data into json
# def convert_write_json(data, json_file):
#     with open(json_file, "w") as f:
#         f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) #for pretty
#         f.write(json.dumps(data))


# read_CSV(file,json_file)

import pandas as pd
import json
filepath = "first_edit.csv"
output_path = "outputfile.json"

df = pd.read_csv(filepath)

# Create a multiline json
json_list = json.loads(df.to_json(orient = "records"))

with open(output_path, 'w') as f:
    for item in json_list:
        f.write("%s\n" % item)