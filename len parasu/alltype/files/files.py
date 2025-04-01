import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist 

# step 1
files = open("names.txt")
# print(files.read())
# print(files.read(4))

# step 2
# print(files.readline())
# print(files.readline())
# print(files.readline())

# step 3
# for line in files:
#     print(line)
# files.close()  # files close comment

# step 4
# try:
#     files = open("names.txt")
#     print(files.read())
# except:
#     print("The file you want to read doesn't exist")
# finally:
#     files.close()

# step 5
# Append - creates the file if it doesn't exist
# files = open("names.txt", "a")
# files.write("\ncss")
# files.close()

