def minimoEjercBien(cantEjer,porcentaje):
    """Recibe:
            cantEjer: <int>
            porcentaje: <int>
       devuelve la cantidad minima de ejercicios
       que se deben hacer bien para aprobar en
       formato integer."""
    minimoEjercBien = (porcentaje * cantEjer) /100
    return int(minimoEjercBien)

def notaFinal(ejerciciosBien,cantEjer):
    """Recibe:
            ejerciciosBien: <int>
            cantEjer: <int>
       convierte la nota final en
       un porcentaje y la devuelve como
       integer."""
    notaFinal = (ejerciciosBien * 100) /cantEjer
    return int(notaFinal)

cantEjer = 0

while cantEjer < 1 or cantEjer == 0:
    cantEjer = int(input("Ingrese la cantidad de ejercicios del examen: "))

porcentaje = int(input("Ingrese el porcentaje para aprobar: "))

ejerciciosBien = 0

while ejerciciosBien != -1:
    ejerciciosBien = int(input("Ingrese la cantidad de ejercicios bien hechos o -1 para finalizar: "))
    
    if ejerciciosBien > cantEjer:
        print("Datos invalidos")
        
    elif ejerciciosBien < -1:
        print("Datos invalidos")
        
    elif ejerciciosBien > minimoEjercBien(cantEjer,porcentaje) or ejerciciosBien == minimoEjercBien(cantEjer,porcentaje):
        print("El alumno aprobó con", notaFinal(ejerciciosBien,cantEjer),"%")
        
    elif ejerciciosBien == -1:
        break
    
    elif ejerciciosBien < minimoEjercBien(cantEjer,porcentaje):
        print("El alumno desaprobó con", notaFinal(ejerciciosBien,cantEjer),"%")