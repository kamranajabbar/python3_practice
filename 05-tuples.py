#Chapter # 20 Tuples

#Bunch of values in a single variable is called "Tuples"
#Tuples in python, is immutable or un-changeable
#We can not add/remove/edit elements after creation of tuple isntance
#We can access, copy and slice a tuple
#Each element in Tuples is called "item"
#Items are defined in "[]" square brakets
#Items are seperated by "," comma
#Tuples can hold Different type of data type values in single Tuples.

tupples = ("Kamran", 100, "Jabbar")
print("Length of tupple : ", len(tupples))

tupples = ("Kamran", 100, "Jabbar")
print("Access an element of tupplevat index 1 : ", tupples[1])

name = "Kamran", 100, "Jabbar", "Kamran", 120, "Kamran", 200, "Kamran"
print("convert into tupple : ", name)
print("Get index of tupple element : ", name.index(100))
print("Get index of tupple element : ", name.index("Jabbar"))
print("Get index of tupple element : ", name.count("Kamran"))