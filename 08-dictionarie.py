#Chapter # 25-40 Dictionaries

#Bunch of values in a single variable is called "Dictionaries"
#Dictionaries in python, is mutable or changeable
#Dictionaries have members that contains keys and values
#Dictionaries does not have index
#We can not add/remove/edit members (key and value) after creation of Dictionaries isntance
#We can access, copy and slice a Dictionaries
#Members (key and value) are defined in "{}" curly brakets
#Members are seperated by "," comma
#Dictionaries can hold Different type of data type members (keys and values) in single Dictionaries.

#get length of dictionary
dictionary = {"name":"Kamran", "age": 19, "gender":"M"} 
print("Length of dictionary : ", len(dictionary))

#add a member (key and value) in existing dictionary
dictionary["email"] = "kamran@gmail.com" 
print("Dictionary after adding email key/value : ", dictionary)

#access a member (value by key) in dictionary 
print("Access dictionary element : ", dictionary['name'])

#access a member (value by key) in (int) in dictionary 
student = {1:"Kamran", 2: "Imran", 3:"Irfan"}
print("student with key 1 : ", student[1])
print("student with key 3 : ", student[3])

#delete/remove a member (value by key) in dictionary 
students = {1:"Kamran", 2: "Imran", 3:"Irfan"}
del students[1]
print("students dictionary : ", students)

#update a member (value by key) in dictionary 
students = {1:"Kamran", 2: "Imran", 3:"Irfan"}
students["4"] = "Rizwan" 
print("students dictionary : ", students)

#Check keys exist in dictionary
name = {1:"Kamran", 2: "Imran", 3:"Irfan"}
print("check key 4 in name dictionary : ", 3 in name)
print("check key 4 in name dictionary : ", 4 in name)

#iterating dictionary
names = {1:"Kamran", 2: "Imran", 3:"Irfan"}
for key in names.keys():
    print("get keys in key dictionary : ", key)

for value in names.values():
    print("get values in value dictionary : ", value)

for key, value in names.items():
    print(f"key {key} : value {value}")

#creating a list holding dictionaries
students = []
students.append("ABC")
students.append({"name":"Kamran", "age":28, "Gender":"Male"})
students.append({"name":"Imran", "age":30, "Gender":"Male"})
students.append("XYZ")
print("Access List of dictionary with index 1 then name : ", students[1]['name'])

#access a memeber from list of dictionaries
for student in students:
    print(student)

#creating a dictionary holding list or list in dictionary
employee = {"Name":"Kamran Jabbar", "ChildrenName":["Noman","Rehman","Ali"], "Gender":"Male"}
print(employee['ChildrenName'][0])
print(employee['ChildrenName'][1])

#creating a dictionary holding dictionaries
employee = {"Name":"Kamran Jabbar", "Children":{"Noman":{"Age":18, "Class":"8th"}, "Affan":{"Age":19, "Class":"9th"}}, "Gender":"Male"}
print("Noman all data : ", employee['Children']['Noman'])
print("Affan Age : ", employee['Children']['Affan']['Age'])

d = {"Kamran":40,"Jabbar":45}
print(d["Kamran"])

aa = {1:"Kamran", 2: "Imran", 3:"Irfan"}
del aa

ds = {1,"A",2}
print(ds)