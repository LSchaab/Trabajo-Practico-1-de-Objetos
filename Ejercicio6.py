multis = []

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
n3 = int(input("Ingrese un numero: "))
n4 = int(input("Ingrese un numero: "))

mult1 = n1 * n2
mult2 = n1 * n3
mult3 = n1 * n4
mult4 = n2 * n3
mult5 = n2 * n4
mult6 = n3 * n4

multis.append(mult1)
multis.append(mult2)
multis.append(mult3)
multis.append(mult4)
multis.append(mult5)
multis.append(mult6)

def compararMultis(multis):
  mayor = multis[0]
  for i in range(len(multis)):
    if multis[i] > mayor:
      mayor = multis[i]
  return mayor

print(compararMultis(multis))
