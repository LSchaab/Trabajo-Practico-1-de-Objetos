numeros = []

for i in range(4):
  numero = int(input("Introduce 4 numeros: ".format(i + 1)))
  numeros.append(numero)



def sacarelmayor(numeros):
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    
    return mayor

print("Mayor:", sacarelmayor(numeros))