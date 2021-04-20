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
            return 1 and aprobarPorc
        else:
            return 0 and aprobarPorc

if correcionExamen(cantEjer,porcentaje,ejerciciosBien)==1:
    print("El alumno no ha aprobado, su nota correspondiente: ",aprobarPorc )
else:
    print("El alumno ha a aprobado", aprobarPorc )