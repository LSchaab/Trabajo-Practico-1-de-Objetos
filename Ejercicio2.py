
def perimetro_rectangulo(b,h):
    """Calcula el perímetro de un rectangulo"""
    perimetro = (b * 2) + (h * 2)
    return perimetro

def area_rectangulo(b,h):
    """Calcula el area de un rectangulo"""
    area = b * h
    return area

def areacoordenadas(y2,y1,x2,x1):
    """ Calcula el area de un rectangulo en base a las coordenadas en los ejes x e y"""
    area = (y2-y1) * (x2-x1)
    return area

def perimetro_circulo(r):
    """Calcula el perimetro de un circulo"""
    perimetro = 2 * 3.14 * r
    return perimetro


def area_circulo(r):
    """Calcula el area de un circulo"""
    area2 = 3.14 * (r**2)
    return area2

def volumen_esfera(r):
    """Calcula el volumen de una esfera"""
    volumen = 4/3 * 3.14 * (r**3)
    return volumen


def hipotenusa(cat1,cat2):
    """Calcula la hipotenusa de un triangulo"""
    hipotenusa = (cat1**2 + cat2**2)**1/2
    return hipotenusa


operacion = int(input("""Ingrese la operacion que desea: 
1.Calcular perímetro de un rectangulo
2.Calcular área de un rectangulo
3.Calcular área de un rectangulo con coordenadas
4.Calcular perímetro de un círculo dado su radio
5.Calcular área de un círculo dado su radio
6.Calcular volumen de una esfera dado su radio
7.Calcular hipotenusa dados los catetos
 """))

if operacion == 1:
    base = int(input("Ingrese la base de su rectangulo: "))
    altura = int(input("Ingrese la altura de su rectangulo: "))
    if altura < 1 or base < 1:
        print("No ingrese numeros negativos.")
    else:
        print("El perimetro es: ",perimetro_rectangulo(base,altura))

if operacion == 2:
    base = int(input("Ingrese la base de su rectangulo: "))
    altura = int(input("Ingrese la altura de su rectangulo: "))
    print("El area de su rectangulo es:",area_rectangulo(base,altura))

if operacion == 3:
    y2 = int(input("Ingrese la coordenada y2: "))
    y1 = int(input("Ingrese la coordenada y1: "))
    x2 = int(input("Ingrese la coordenada x2: "))
    x1 = int(input("Ingrese la coordenada x1: "))
    print("El área de su rectangulo es: ", areacoordenadas(y2,y1,x2,x1))

if operacion == 4:
    radio = int(input("Ingrese el radio de su circulo: "))
    print("El perímetro de su círculo es: ",perimetro_circulo(radio))

if operacion == 5:
    radio=int(input("Ingrese el radio de su circulo: "))
    print("El área de su círculo es: ",area_circulo(radio))

if operacion == 6:
    radio = int(input("Ingrese el radio de su esfera: "))
    print("El perímetro de su círculo es: ",volumen_esfera(radio))
    
if operacion == 7:
    cateto1 = int(input("Ingrese la medida del cateto 1: "))
    cateto2 = int(input("Ingrese la medida del cateto 2: "))
    print("El valor de la hipotenusa es: ", hipotenusa(cateto1,cateto2))
