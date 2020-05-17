import math

def r_okregu(a,b,x,y):
    r = math.sqrt((x-a)**2 + (y-b)**2)
    return r

a = int(input("a:"))
b = int(input("b:"))
x = int(input("x:"))
y = int(input("y:"))

print(str(r_okregu(a,b,x,y)))