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

# step 6
# f = open("context.txt","w")
# f.write("I deleted all of the context")
# f.close()

# step 7
# Two ways to create a new file
# Opens a file writing, creates the file if it does not exist
# f = open("name_list.txt","w")
# f.close()

# step 8
if not os.path.exists("dave.txt"):
    f = open("dave.txt","x")
    f.close()

# step 9
# alrededy files is avalabi not a creats
# f = open("dave.txt","x")
# f.close()

# step 10
# Delete a files
# Avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")

# step 11
# With has built-in implicit exception handling
# close() will be automatically called
with open("more_named.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)