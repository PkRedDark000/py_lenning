## step 1
try:
    print(x)
except:
    print("error")

## step 2

try:
    print(x)
except Exception as error:
    print(error)

## step 3

try:
    print(x)
except NameError:
    print("Name chihck with name")
except Exception as error:
    print("error")

## step 4
x = 2
try:
    print(x)
except NameError:
    print("Name chihck with name")
except Exception as error:
    print("error")

else:
    print("No Error")
finally:
    print("I'm going to print with or without an error.")

