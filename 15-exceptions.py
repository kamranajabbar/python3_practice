#Chapter # 77 Exceptions

#76: Planning for things to go wrong
#77: A more practical example of exception handling

#NOTE
#Exceptions are run time errors
#We know that compile time error are syntax error

# Use of 'finally'
try:
    value1 = int(input("Enter a number :"))
    value2 = int(input("Enter another number :"))

    ans = value1/value2
except Exception as e:
    print(f"Exception handled >> {(e)}")
else:
    print("if exception will not throug then else will run ", ans)
finally:
    print("Finally will always run")