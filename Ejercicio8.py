ValorLetras = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def convertRoman(num):
    """Recibe:
            num: <int>
       recorre la lista con tuplas y mientras
       el valor ingresado sea mayor a los numeros
       de las tuplas, se le resta ese valor al numero
       y se agrega la letra (r) equivalente al numero (i)
       en la lista a la string 'roman'.
       Devuelve la string 'roman'. """
       
    roman = ""

    while num > 0:
        for i, r in ValorLetras:
            while num > i or num == i:
                roman = roman + r
                num = num - i

    return roman

añoValido = False

while añoValido == False:
    try:
        num = int(input("Ingrese un numero: "))
        if num < 0:
            print("Año no valido.")
        else:
            añoValido = True
            break
    except ValueError:
        print("Año no valido.")

print("Su numero en numeros romanos es: ", convertRoman(num))