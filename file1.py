#the argument inside read function denotes the characters inside the file. 
file1 = open("operate.txt","r")
print(file1.read(20))
file1.close()

file2 = open("operate.txt","r")
print(file2.readline())
file2.close()

file3 = open("operate.txt", "r")

for x in file3:
    print(x)

file3.close()

file4 = open("operate.txt","r")
print(file4.readlines())
file4.close()

#removing lines from file

file5 = open("operate.txt","r")
file6 = open("updated.txt","w")

for line in file5.readlines():
    if line.startswith("Then"):
        print(line)
        file6.write(line)

    

file5.close()
file6.close()

file7 = open("operate.txt","r")
file8 = open("fresh.txt","w")

contents = file7.readlines()
print(type(contents))

for i in range(1,len(contents)+1):
    if (i%2 != 0):
        file8.write(contents[i-1])
    else:
        pass

file7.close()
file8.close()