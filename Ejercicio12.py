palabra = input("Ingrese una palabra: ")

contA = 0
contE = 0
contI = 0
contO = 0
contU = 0 

for i in palabra:
    if i == "a" or i == "A":
        contA = contA + 1
    if i == "e" or i == "E":
        contE = contE + 1
    if i == "i" or i == "I":
        contI = contI + 1
    if i == "o" or i == "O":
        contO = contO + 1
    if i == "u" or i == "U":
        contU = contU + 1

print("Cantidad a:", contA, "Cantidad e:", contE, "Cantidad i:",contI , "Cantidad o:" , contO, "Cantidad u:", contU)