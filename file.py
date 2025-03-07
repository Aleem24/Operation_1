file1 = open("operate.txt","r")
# print(filefor line in file5.readlines():
    # i1.read(19)) # The arguement inside read function denotes the characters inside the file.
# print(file1.readline())
file1.close()
file2 = open("operate.txt","r")
file2.close()

file3 = open("operate.txt","r")

# for _ in range(4):
    # print(file3.readline())




# file4 = open("operate.txt","r")
# print(file4.readlines())
# file4.close()


# Removing lines from a file

file5 = open("operate.txt","r")
file6 = open("updated.txt","w")

# f not(line.startswith("We")):
        # print(line)

    # file6.write(line)

# file5.close()
# file6.close()

file7 = open("operate.txt","r")
file8 = open("fresh.txt","w")

contents = file7.readlines()
print(type(contents))

for i in range(1, len(contents)+1):
    if (i%2 != 0):
        file8.write(contents[i-1])
    else:
        pass

file7.close()
file8.close()
