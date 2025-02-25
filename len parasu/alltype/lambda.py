sqared = lambda num : num * num
print(sqared(3))

add_two = lambda num : num + 2

print(add_two(8))

sum_totel = lambda a, b : a + b
print(sum_totel(5, 5))

# def sum_test ( a , b):
#     return a + b

print ("parasu hack")

def funcBuilder(x):
    return lambda num : num + x

add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(7))