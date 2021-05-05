multis = []

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
n3 = int(input("Ingrese un numero: "))
n4 = int(input("Ingrese un numero: "))

while multis.index != 6:
  mult1 = n1 * n2
  multis.append(mult1)
  mult2 = n1 * n3
  multis.append(mult2)
  mult3 = n1 * n4
  multis.append(mult3)
  mult4 = n2 * n3
  multis.append(mult4)
  mult5 = n2 * n4
  multis.append(mult5)
  mult6 = n3 * n4
  multis.append(mult6)
  break

def compararMultis(multis):
  """Recibe una lista, la recorre y devuelve el valor mayor"""
  
  mayor = multis[0]
  
  for i in range(len(multis)):
    if multis[i] > mayor:
      mayor = multis[i]
      
  return mayor

print("El mayor producto que se puede obtener de los numeros ingresados es: ", compararMultis(multis))
