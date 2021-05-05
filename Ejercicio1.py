nombre = input("Ingrese su nombre: ")

print("Hola,", nombre)

numerosValidos = False

while numerosValidos == False:
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        numerosValidos = True
        producto = num1 * num2
    except ValueError:
        print("Numero no valido.")


print("El producto de", num1,"multiplicado por", num2, "es", round(producto,2))