import random


class Student:

    # Default Constructor : Used for Initializing the Objects

    def __init__(self, empId, empName):
        self.empId = empId
        self.empName = empName


s1 = Student(random.randrange(8900, 9800), "Tom")

print(" Getting Employee Information : ", s1.empName)

print(s1.empId)
print(s1.empName)


s2 = Student(random.randrange(7000, 10000), "Peter")

print(" Getting Employee Information : ", s2.empName)

print(s2.empId)
print(s2.empName)
