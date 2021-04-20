def factorial(numero):
    fact=numero
    for i in range (1,numero):
        fact=fact*i
    return fact

n=int(input("Ingrese el numero del cual quiere su factorial: "))
print("El factorial del numero ingresado es: ", factorial(n))

