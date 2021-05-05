palabra = input("Ingrese una palabra: ")
vocales = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0 

for i in palabra.lower():
    if i in vocales:
        vocales[i] = vocales[i] + 1

print("Cantidad a:", vocales["a"], ", Cantidad e:", vocales["e"], ", Cantidad i:",vocales["i"] , ", Cantidad o:" , vocales["o"], ", Cantidad u:", vocales["u"])