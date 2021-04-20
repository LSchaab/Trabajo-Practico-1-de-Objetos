"""
1: Cantidad de ejerciciso de un examen
2: porcentaje necesario de los ejercicios pa aprobar
3: Cantidad de ejercicios correctos
4: Aprobado o no
5: valor centinela(palabra para salir del programa)
de uso exclusivo para el profe fav FEFE y LuciANO CARERA
"""

cantEjer = int(input("Ingrese la cantidad de ejercicios del examen: "))
porcentaje = int(input("Ingrese el procentaje necesario para aprobar: "))

def notaMinima(cantEjer,porcentaje):
    notaMinima= (porcentaje*cantEjer)/100
    return notaMinima

def correcionExamen(cantEjer,porcentaje,ejerciciosBien):
    ejerciciosBien=input("Ingrese la cantidad de ejercicios bien: ")
    while ejerciciosBien != "salir":
        aprobarPorc= (ejerciciosBien*100)/cantEjer
        if aprobarPorc < notaMinima(cantEjer,porcentaje):
            return 1
        else:
            return 0

print("")