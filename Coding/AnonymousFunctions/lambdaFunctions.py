import random

num = [2, 3, 9, 4, 6, 8, 10, 12, 15, 16, 18, 21, 22]

# using filter : we will filter the odd number which are divisible by only 3

odd_list = list(filter(lambda n: n % 3 == 0, num))
print(odd_list)

even_list = list(filter(lambda n: n % 2 == 0, num))
print(even_list)

double_list = list(map(lambda a: a * 2, num))
print(double_list)

# storing in dictionary using lamda map functions

userInfo = {

        1: random.randrange(20000, 40000),
        2: random.randrange(80000, 120000),
        3: random.randrange(2000, 4000),
        4: random.randrange(10000, 12000),
        5: random.randrange(8000, 12000),
}

print(userInfo)
print("#################")

