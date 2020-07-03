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
    return ans, "KJ", True, 3.142

re = add_numbers(2,4)
print("Print return value from function : ", re)

#Functions as a variables
def adds(a,b):
    return a+b
def subs(a,b):
    return a-b

result = adds(2,2) + subs(10,2)
print(result)

#function with local and global variables
#function with local variable
def beHappy():
    name = "Mr Kamran"
    print(f"{name} is very happy today.")

beHappy()

#function with global variable
anotherName = "Mr ABC"
def Sad():
    print(f"{anotherName} is not happy today!")

Sad()
print(anotherName)


#functions within functions
def commissionCalc(sales):
    if sales > 100:
        return sales * 100
    elif sales > 50:
        return sales * 50
    elif sales > 20:
        return  sales * 20
    else:
        return 0

def salaryCalc(basic,sales):
    grossSalary = basic + commissionCalc(sales)
    print(f"Your gross salary is {grossSalary}")

salaryCalc(50000,150)