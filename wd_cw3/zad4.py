
print("y=a*x+b")
a = int(input("a:"))

def funkcja(a):
    if a > 0:
        print("Funkcja jest rosnąca")
    elif a < 0:
        print("Funkcja jest malejąca")
    else:
        print("Funkcja jest stała")

funkcja(a)