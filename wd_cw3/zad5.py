print("funkcja1: y=a1*x+b1")
print("funkcja1: y=a2*x+b2")

a = int(input("a1:"))
b = int(input("a2:"))

def proste(a1, a2):

    if a1 == a2:
        print("Funckje są równoległe")
    elif a1*a2 == -1:
        print("Funckje są prostopadłe")

proste(a,b)