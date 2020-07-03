#Chapter # 24 String changing case

name = "Kamran"
print("String in Upper Case : ", name.upper())
print("String in Lower Case : ", name.lower())
print("String in Capitale Case : ", name.capitalize())
print("String in Title Case : ", name.title())

str = "hello"
print(str[:2])

string = "my name is x"
for i in string.split():
    print(i, end=", ")

print("\n")
x=1
y=2
z=x
x=y
y=z
print(x,y)

A = 16
B = 15
print(A % B // A)

print("-------- Q14 -----")
for i in range(10):
    if i == 5:
        break
    else:
        print(i)
else:
    print("Here")

print("-------- Q15 -----")
list1 = [1, 3, 2]
print(list1 * 2)

print("-------- Q16 -----")
a = {}
a[1] = 1
a['1'] = 2
a[1] = a[1]+1
count = 0
for i in a:
    count += a[i]
print(count)

print("-------- Q17 -----")
numbers = [1,2,3,4]
numbers.append([5,6,7,8])
print(len(numbers))

print("-------- Q18 -----")
names = ['Amir','Bear','Chariton','Daman']
print(names[-1][-1])

print("-------- Q19 -----")
names = [1,2,3,4]
print(names[-3:-2])

print("-------- Q20 -----")
abc = {"KJ":78}
xyz = {"AJ":156}
print(abc == xyz)

print("-------- Q22 -----")
x = 1 / 2.0 + 3//3 + 4 ** 1
print(x)

print("-------- Q23 -----")
a = [11,2,23]
b = [11,2,2]
print(a  < b)

print("-------- Q24 -----")
a = {1:5,2:3,3:4}
a.pop(3)
print(a)

print("-------- Q27 -----")
abc = {"KJ":40, "AJ":45}
print("KJ" in abc)

print("-------- Q29 -----")
s1 = [3,4]
s2 = [1,2]
s3 = list()
i=0
j=0
for i in s1:
    for j in s2:
        s3.append((i,j))
        i +=1
        j +=1
print(s3)