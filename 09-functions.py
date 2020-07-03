#Chapter # 41-50 Functions
#default parameters must be placed in last
#arbitrary arguments must be placed in last

#Basic function
print("A line before function")
def add():
    print(2+5)

add()
print("A line after function \n")

#function with arguments
def addNumbers(number1, number2):
    re = (number1 + number2)
    print(re)

addNumbers(10, 10)

#positional arguments
def full_name(fname, mname, lname):
    print(fname + mname + lname)

full_name("kamran", "abddul", "jabbar")

#key-word arguments
def city_name(first, second, third):
    print(first + " " + second + " " + third)

city_name(second="Islamabad", first="Karachi", third="Lahore")
city_name("Islamabad", "Karachi", third="Lahore")
city_name("Islamabad", second="Karachi", third="Lahore")

#default value parameters
def address(house, city, country, street="Street NA"):
    print(house + " " + street + " " + city + " " + country)

address("House # 135", "Karachi", "Pakistan")
address("House # 135", "Karachi", "Pakistan", "Street # 1")

#Dealing with an unknown (arbitrary) numbers of arguments
def pizzaOrder(size, flavour, *toppings):
    print(f"Your order for pizza of size {size} inch and flavour {flavour} with toppings {toppings} is ready to deliver!")

pizzaOrder(12, "BBQ", "Olives", "ABC", "XYZ")

#Passing information back from them (return value from function)
def add_numbers(val1, val2):
    ans = val1 + val2
    return ans

re = add_numbers(2,4)
print("Print return value from function : ", re)