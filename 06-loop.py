#Chapter # 21,22,23,51,52 Loops and type casting

for a in range(5):
    print(a, "=> Kamran =>", a)

for num in range(5):
    print("Number =>", num)

for num in range(5, 10):
    print("With Start and End Range => ", num)

for num in range(1, 10, 2):
    print("With Start,End and Steps Value in Range => ", num)

for num in range(10, 1, -2):
    print("With Start,End and Steps Value in Range In Reverse Order => ", num)

cities = ["Karachi", "Lahore", "Islamabad", "Multan"]
for city in cities:
    print(f"Top COVID-19 effected city is {city}")

for num in ["111", "222", "333", "444"]:
    print(f"Top COVID-19 numbers is {num}")

#If for loop find single string in varibale, it will loop each charaters of the same string
country = "Pakistan"
for element in country:
    print(f"Chars {element}")

#If for loop find multiple strings in varibale, it will loop each string
country = "Pakistan", "UK", "USA"
for element in country:
    print(f"String {element}")

#If for loop with break
country = "Pakistan", "UK", "USA", "KSA", "UAE"
for element in country:
    if element == "USA":
        break
    print("Print element with break : ", element)


#If for loop with continue
country = "Pakistan", "UK", "USA", "KSA", "UAE"
for element in country:
    if element == "USA" or element == "UAE":
        continue
    print("Print element with continue : ", element)

#Nested Loop
for num in range(5):
    print("Inner loop start")
    for char in "China":
        print(num, char)

#Table print with loop
# table_number = int(input("Enter Table Number"))
# for a in range(1,11):
#     print(f"{table_number} * {a} = {table_number*a}")

#Type casting
#user_input1 = input("Enter Something : ")
#print("Enter some thing = ", type(user_input1))

#user_input2 = int(input("Enter Something : "))
#print("Entered value value = ", type(user_input2))

#user_input3 = float(input("Enter Something : "))
#print("Entered value type = ", type(user_input3))

#While Loop
#Example 1
a = 0
while a <= 10:
    print(a, "Print while loop")
    a += 1

#Example 2
flag = True
favFoods = []

while flag:
    user_input = input("Enter food name : ")
    if user_input == "Q":
        flag = False
    else:
        favFoods.append(user_input)

print("Your Entered Food Name Is: ",favFoods)