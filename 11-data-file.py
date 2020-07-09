#Chapter # 62-65 Data Files

#62: Data files
#63: Data files: Storing data
#64: Data files: Retrieving data
#65: Data files: Appending data

#Read file
with open("filename.txt", "r") as file:
    content = file.read()
print(content)

#Write data in file
with open("filename.txt", "w") as file:
    file.write("Line 2 added \n")

#Append data in file(none existing file)
with open("filename1.txt", "a") as file:
    file.write("Line 3 added \n")

#Append data in file(on existing file)
with open("filename.txt", "a") as file:
    file.write("Line 4 added \n")

#In w+ Mode (Read and Write Functions works)
with open("filename.txt", "w+") as file:
    file.write("New line added \n")
    content = file.read()
print(content)

#In r+ Mode (Read and Write Functions works) (Note file must be created in r and r+ mode)
with open("filename.txt", "r+") as file:
    file.write("Another new line added \n")
    file.write("Another new line added \n")
    file.write("Another new line added \n")
    file.write("Another new line added \n")
    file.write("Another new line added \n")

    #file.seek(0)
    content = file.read()
print(content)
