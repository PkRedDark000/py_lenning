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


numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map (lambda num : num * num, numbers)

print(list(squared_nums))

odd_nums = filter(lambda num: num % 2 != 0,numbers)
print(list(odd_nums))

from functools import reduce

numbers = [1,2,3,4,5,1]
totel = reduce(lambda acc, curr: acc + curr, numbers)
print(totel)

print(sum(numbers))

names = ['parasu ','kaviya ','parthiban ']
char_count = reduce(lambda acc, curr: acc + len (curr),names,0)
print (char_count)

names = ['parasu ','kaviya ','parthiban ']
char_count = reduce(lambda acc, curr: acc + len (curr),names,2)
print (char_count)