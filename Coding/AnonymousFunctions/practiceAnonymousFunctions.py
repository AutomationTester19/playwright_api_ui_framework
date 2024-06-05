# Anonymous functions are without function name, only expression and return type is declared

# normal function

def isEven(n):
    return (n * 2) % 2 == 0


result = isEven(20)
print(result)

# Lambda Expressions:
val = lambda a, b: (a + b) % 2 == 0
res = val(10, 20)
print(res)
