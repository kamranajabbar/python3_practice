a = ['a','b','c','d','e']

while a:
    if len(a) < 3:
        break
    print(a.pop(), end=" ")
print("Done")

#print("hwllow" + 2 + "world")

#Q8
fo = open("myfile.txt","w+")
print("Name of the file: ", fo.name)
seq = "PIAIC\nHello Viewer!!"
fo.writelines(seq)
fo.seek(0,0)
for line in fo:
    print(line)

fo.close()

#Q10
import os

def read_file(file):
    line = None

    if os.path.isfile(file):
        data = open(file, "r")

    while line != '':
        line = data.readline()
        print(line)


#Q12
def outerFunction():
    global a 
    a = 20
    
    def innerFunction():
        global a
        a = 30
        print('a=', a)

a =10
outerFunction()
print('a=', a)

#Q13
s = ""
n = 5

while n > 0:
    n -= 1
    if(n % 2) == 0:
        continue

    a = ['a','b','c']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break

class ABC():
    def __init__(self):
        self.a = "A"

obj1 = ABC()
print(obj1.a)

obj1.b = "B"
print(obj1.b)

d = {'foo':1, 'bar':2, 'baz':3}
while d:
    print(d.popitem())
print("Done")