import random 
from random import randrange

num = random.randrange(1 , 5)
n = 0

while n != num:
    n = int(input("Ingrese un numero: "))
    if n == num:
        print("Muy bien")
        break
    elif n > num:
        print("El numero es menor.")
    elif n < num:
        print("El numero es mayor.")