Entorno1 = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

def Aspirar_entorno(Entorno):
    
    while 0 in Entorno.values():
        
        for habitacion in Entorno:
            if Entorno[habitacion] == 0:
                print("Aspirando habitacion:" , habitacion)
                Entorno[habitacion] = 1
            
    print("Las habitaciones fueron limpiadas")
    return 1
                                  
Valo_entregado = Aspirar_entorno(Entorno1)
          
            



##print(Entorno)
##Aspiradora = len(Entorno)
##contador = 0

##for habitacion in Entorno:
##    if Entorno[habitacion] == 0:
##        print("Aspirando habitacion:" , habitacion)
##        habitacion = 1

## for habitacion in Entorno:
##        if Entorno[habitacion] == 0:
##            print("Habitacion limpia: " , habitacion)
##            contador +=1
##        if contador == Aspiradora:
##            print("Las habitaciones fueron limpiadas")
            