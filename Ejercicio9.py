CONTRASEÑA= "odiamospython"

def comprobarContraseña(cont):
    if cont==CONTRASEÑA:
        return True
    else:
        return False

import time
from time import sleep
intentos=0
cont=""

while cont != CONTRASEÑA:
    cont=input("Ingrese la contraseña: ")
    intentos=intentos+1
    time.sleep(intentos+1)
    if comprobarContraseña(cont)==True:
        print("Muy bien capo, orgullosa de vos estoy")
        break
    else:
        if intentos==3:
            print("No tiene más intentos.")
            break

