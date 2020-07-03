#Chapter # 15,16,17,18,19 List

#Bunch of values in a single variable is called "List"
#List in python, is mutable or changeable
#Each element in list is called "item"
#Items are defined in "[]" square brakets
#Items are seperated by "," comma
#List can hold Different type of data type values in single list.

#String List
name = ['Kamran','Imran','Adnan']
#access list
print("List: ", name)

#access element by index
print("Element at index 1: ", name[1])

#get list lenght
print("Length of list : ", len(name))

#add (append) a member in the list (NOTES: append can only add single element in list)
name.append("Kashan")
print("List after adding (appending) an element : ", name)

#add (insert) a member in the list (NOTES: insert can only add single element in list)
name.insert(2, "Irfan")
print("List after adding (inserting) an element : ", name)

#add (extend) more then one members in the list (NOTES: extend can  add one or more then one elements in list, and have append behavior)
name.extend(["Rizwan","Affan","Noman"])
print("List after adding (inserting) an element : ", name)

#count each value (NOTES: entered value must be case sensitive)
print("Count entered value (without case sensitive) in list : ", name.count("kamran"))
print("Count entered value (with case sensitive) in list : ", name.count("Kamran"))

#Index function given index status
print("Get index number of 'Adnan' in list : ", name.index("Adnan"))

#Clear function remove all elements in list (List will be empty permentlay)
#print("Remove all elements in list : ", name.clear())

#Copy function remove make copy same list
name2 = name.copy()
print("name list : ", name)                     #By value
print("name2 list (By value) : ", name2)

name3 = name
print("name3 list (By reference) : ", name3)    #By reference

#Check name3 list after append new value
name3.append("Khan")
#As we know that name3 is copy by reference from name list, therefore, name and name3 list will be same after append new value in name3 list.
print("Print name3 list : ", name3)
print("Print name list : ", name)

#As we know that name2 is copy by value from name list, therefore, name list will not chnaged after append new value in name2 list.
print("Print name2 list : ", name2)

#del is statement, not called function, and used to remove/delete item permently from a list, del required index to delete item
fruits = ['Apple','Mango','Banana']
del fruits[0]
print("Print fruits list after delete value with index 0 : ", fruits)

#remove function used to remove/delete value from a list, it requires value of item to delete from list
fruits1 = ['Apple','Mango','Banana']
fruits1.remove('Mango')
print("Print fruits list after delete value : ", fruits1)

#pop function used to remove/delete item by from a list, as it popped item from the end of the list (based on LIFO), as pop can take index (optional) to delete item
cities = ['Karachi','Lahore','Islamabad','Multan','Quetta']
popped_city = cities.pop()
print(f"This city is popped from list '{popped_city}'")
print(f"The remaining cities are {cities}")
popped_city = cities.pop()
print(f"This city is popped from list '{popped_city}'")
print(f"The remaining cities are {cities}")
popped_city = cities.pop(1)
print(f"This city is popped from list '{popped_city}'")
print(f"The remaining cities are {cities}")

#Sort function used to sort list with Acending order
fruits3 = ['Apple','Mango','Banana']
fruits3.sort()
print("List after sort (ACS) : ", fruits3)
fruits3.sort(reverse=True)
print("List after sort (DESC) : ", fruits3)

#Reverse function used to reverse sorting
alphabats = ['A','B','C','D','E']
alphabats.reverse()
print("List after reverse : ", alphabats)

alphabats = ['E', 'D', 'C', 'B', 'A']
alphabats.reverse()
print("List after reverse : ", alphabats)

#List slicing
#alphabats = [-5,  -4,  -3,  -2,  -1]      Nagitive index
#alphabats = [ 1,   2,   3,   4,   5]      Positive index
alphabats  = ['A', 'B', 'C', 'D', 'E']

print("Get value from A to D with +ve index : ", alphabats[0:4])
print("Get value from B to C with +ve index : ", alphabats[1:3])

print("Get value from B to C with -ve index : ", alphabats[1:3])

print("List slicing : ", alphabats[:])
print("List slicing : ", alphabats[3:])
print("List slicing : ", alphabats[:3])
print("List slicing : ", alphabats[2:-1])
print("List slicing : ", alphabats[2:-5])   #only farward index allowed

#Integer list
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("List slicing with steps value 1 : ", numbers[0:10:1])
print("List slicing with steps value 2 : ", numbers[0:16:2])
print("List slicing with steps value 5 : ", numbers[::5])


#float list
float_numbers = [11.2, 2.22, 3.10, 7.7]

#mix list
mix_list = [12, "Kamran", 3.10, True, "Jabbar"]