courseTuple = ("Kubernetes", "Docker", "AWS", "Python")

#


print(courseTuple)
print(len(courseTuple))  # 4

# Accessing the tuples

print(courseTuple[1])

# Accessing with invalid index

# print(courseTuple[9])  # Tuple index out of range

# updating the tuple values
# Tuples are immutable in nature
# We cannot change the value, once it is declared
# courseTuple[2] = "Azure"
# print(courseTuple)
# we can convert tuple to list and then change the value
# Looping tuples
for val in courseTuple:
    print(val)

print("##### METHODS IN TUPLES #######")

# Methods in tuple:

# 1. Index :  It will display the index or position of particular value from tuple
#             Works with only Integers or Slices
empId_tuple = (2839, 7898, 2456, 3456, 2839)
print(empId_tuple.index(2839))

# 2. Count : It will count the specific value from tuple in tuple

print(empId_tuple.count(2839))

# Join the tuples using + operator

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c", "d")

tuple3 = tuple1 + tuple2
print(tuple3)

# unpacking the tuples:
# Normally when we create tuple, we assign the values to it, which is packing in tuples
# But for unpacking , we can assign the values of tuples using variables using below
fruits = ("apple", "banana", "mango")
print(fruits)
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
