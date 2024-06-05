import random


def empDetails(employeeType, empId, empName):
    print("#### Getting Employee Information ####")

    if employeeType == "EX":
        print("Please Provide Your Existing Employee ID : ")

    elif employeeType == "Full Time":
        print("Generate New Employee ID ")

    else:
        print("Contractors Don't Have Employee ID")

    print(" Employee Id : ", empId)
    print(" Employee Name : ", empName)
    print(" Employee Type : ", employeeType)


# Basic Class, Objects & Method Understanding

class Employee:
    empDetails("EX", random.randrange(1234, 293939), "Tom")
    empDetails("Full Time", random.randrange(1234, 293939), "Peter")
