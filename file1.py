
file1 = open("new_file.txt","r")
# print(file1.read(4))#the argument inside read function denotes the characters inside the file.
file1.close()

file2 = open("new_file.txt","r")
# print(file2.readline())
file2.close()

file3 = open("new_file.txt", "r")

# for x in file3:
#     print(x)

file3.close()

file4 = open("new_file.txt","r")
# print(file4.readlines())
file4.close()

#removing lines from file

file5 = open("new_file.txt","r")
file6 = open("updated_file.txt","w")

for line in file5.readlines():
    if line.startswith("We"):
        # print(line)
        file6.write(line)

    

file5.close()
file6.close()

file7 = open("new_file.txt","r")
file8 = open("fresh_file.txt","w")

contents = file7.readlines()
print(type(contents))

for i in range(1,len(contents)+1):
    if (i%2 != 0):
        file8.write(contents[i-1])
    else:
        pass

file7.close()
file8.close()