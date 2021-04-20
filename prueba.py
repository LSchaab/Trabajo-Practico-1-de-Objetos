cantEjer = int(input("Ingrese la cantidad de ejercicios del examen: "))
porcentaje = int(input("Ingrese el procentaje necesario para aprobar: "))

def notaMinima(cantEjer,porcentaje):
    notaMinima= (porcentaje*cantEjer)/100
    return notaMinima

def correcionExamen(cantEjer,porcentaje):
    ejerciciosBien=input("Ingrese la cantidad de ejercicios bien: ")
    while ejerciciosBien != "salir":
        aprobarPorc= (ejerciciosBien*100)/cantEjer
        if aprobarPorc < notaMinima(cantEjer,porcentaje):
            return 1 
            return aprobarPorc
        else:
            return 0
            return aprobarPorc

if correcionExamen(cantEjer,porcentaje)==1:
    print("El alumno no ha aprobado, su nota correspondiente: ",aprobarPorc )
else:
    print("El alumno ha a aprobado", aprobarPorc,"ha aprobado" )