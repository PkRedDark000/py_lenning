# # dictionaries
# car = { 

#     "brand": "Tesla",
#     "model": "Model_3_P",
#     "year" : 1964 ,
# }
# car2 = dict(brand="Tesla",model="Model_3_P")
# car3 =(car2.copy())
# print(car)
# print(car2)
# print(type(car))
# print(type(car2))
# print(len(car))
# print(len(car2))

# # Access items
# print(car["brand"])
# print(car.get("model"))

# # list all keys
# print(car.keys())
# print(car.values())

# # list of key/values pairs as tuples
# print(car.items())

# # verify a key exists
# print("model" in car)
# print("price" in car)

# # change values
# car["brand"] = "Nio"
# print(car)
# car.update({"price": "400000$"})
# print(car)
# car.update({"brand": "Tesla"})
# print(car)
# car ["Ev"]="Yes" 

# # Remove items
# print(car.pop("price"))
# print(car)
# print(car.popitem())  #Tuple
# print(car)

# # Delete and clear
# car ["Ev"]="Yes"
# del car["Ev"]
# print(car)
# car2.clear()
# print(car2)
# del car2
# print(car3)

# # create a reference
# car2 = car

# print("Bed Copy")
# print(car2)
# print("Bed Copy")
# print(car)
# car2["EV"] = "NO"
# print(car)

# # copy
# car2 = car.copy()
# car2["EV"] = "NO"
# print(car)
# print(car2)

# # or use the dict () constructor function
# car4 = dict(car)
# print(car4)

# # Nested dictionaries
# member1 = {
#     "name": "plant",
#     "instrument":"brend"

# }
# member2 = {

#     "name": "Page",
#     "instrument": "model"

# }
# bard = {
#     "member1": member1,
#     "member2": member2
# }
# print(member1)
# print(member2)
# print(bard)
# print(bard["member1"])
# print(bard["member1"]["name"])
# print(bard["member2"]["instrument"])