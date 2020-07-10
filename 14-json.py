#Chapter # 74-75 JSON

#74: How to save a Python list or dictionary in a file: JSON
#75: How to retrieve a Python list or dictionary from a JSON file

import json

#Write/Overwrite data in json file
with open("jsonfile.json", "w") as file:
    json.dump([2010, 2011, 2012, 2013, 2014], file)

#read data from json file
with open("jsonfile.json", "r") as file:
    data = json.load(file)
    print(data)

#Write dictionary data in json file
customer = {"Name":"Kamran Jabbar", "Age":30, "Education":"MSC", "Address":"Altaf Town"}

with open("jsonDictionary.json", "w") as file:
    json.dump(customer, file)

#Read dictionary data from json file
with open("jsonDictionary.json", "r") as file:
    data = json.load(file)
    print(data)
