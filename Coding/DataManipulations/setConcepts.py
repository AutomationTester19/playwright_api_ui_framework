coursesSet = {"Playwright", "MicroServices", "Kubernetes", "Docker", "AWS", "Docker"}

print(coursesSet)

# Sets :
# 1. sets are unordered
# 2. sets doesn't allow to change the values, once it is assigned
# 3. sets doesn't allow duplicate values

print(len(coursesSet))

# coursesSet[4] = "Azure" # values cannot be change

print(coursesSet)  # no duplicate values

# print(coursesSet[0])  # no, we cannot get the value using index, sets are unordered

# Loops

for val in coursesSet:
    print(val)

# removing items from sets

coursesSet.remove("Docker")

print(coursesSet)

coursesSet.add("Docker")
print(coursesSet)

# Join Sets Methods :
# 1. Union or | operator
# 2. Update
# 3. Intersection or & operator
# 4. Intersection Update
# Joining the sets, using union method we can add another set and union returns the new set

fruit_set = {"apple", "banana", "mango", "cherry"}
alpha_set = {'a', 'b', 'c', 'd'}
print("###### USING UNION METHOD ###############")
final_set = fruit_set.union(alpha_set)
print(final_set)

final_set = fruit_set | alpha_set
print(final_set)
# we can join the set using update method, but it doesn't have return type
print("###### USING UPDATE METHOD ###############")

new_set = fruit_set.update(alpha_set)
print(new_set)  # returns none
print(fruit_set)  # all the values of set 2 will be added to set 1

# Intersection :  returns a new set, and it contains only common items from both the sets
print("###### USING INTERSECTION METHOD ###############")

set1 = {"apple", "cherry", "banana"}
set2 = {"Docker", "Kubernetes", "cherry"}

set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

# Intersection Update : It will keep only duplicate items from set,instead of returning a new set, it will change the
#                        first set
print("###### USING INTERSECTION UPDATE METHOD ###############")

set_A = {"a", "b", "c"}
set_B = {"Docker", "Kubernetes", "a"}

set_A.intersection_update(set_B)
print(set_A)


set_C = {'A', 'B', 'C', 'A', 'D', 'E'}

# pop method removes the random element from set
set_C.pop()

print(set_C)