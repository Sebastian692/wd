import math

def przeciw_prostok(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

a = int(input("a:"))
b = int(input("b:"))

print(str(przeciw_prostok(a,b)))