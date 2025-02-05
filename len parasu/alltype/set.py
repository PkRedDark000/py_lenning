# # Sets
# nums = {1,2,3,4}
# nums2 = set((1,2,3,4))
# print(nums)
# print(nums2)
# print(type(nums2))
# print(len(nums2))

# # No duplicate allowed
# nums = {1,2,2,3}
# print(nums)

# # Ture is a dupe of 1, False is a dupe of zero
# nums = {1,True, 2,False, 3,4,0}
# print(nums)

# # check if a value is in a set
# print(2 in nums)

# # But You cannot refer to an element in the set with an index position or a key

# nums.add(8)
# print(nums)

# # Add element from one set to another 
# morenums = {5,6,7}
# nums.update(morenums)
# print(nums)

# # you can use updata with lists, tuples, and dictionaries, too.
# # merge two set to create a new set 
# one = {1,2,3}
# two = { 5,6,7}

# mynewset = one.union(two)
# print(mynewset)

# #  Keep only the duplicates
# one = {1,2,3}
# two = {2,3,4}
# one.intersection_update(two)
# print(one)

# # keep everything except the duplicates
# one = {1,2,3}
# two = {2,3,4}
# one.symmetric_difference_update(two)
# print(one)