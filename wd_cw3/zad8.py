def suma_c(a1=1,r=1,ile=10):
    suma = 0
    for x in range(a1,ile+1,r):
        suma += x
    return suma

print(suma_c(3,1,4))