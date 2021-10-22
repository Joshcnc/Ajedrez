#################################################################

########           Que necesito hacer?            ###############
#####        tablero funcional y organizado          ###########
###       movimiento de piezas segun las reglas        #########
########          logica de comer piezas      ##################

################################################################

### para comer, ver si la parte final es diferente


### Definicion de las listas que van a conformar el tablero
tablero = [
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ],
    
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ],
    
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ], 
    
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ],
    
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ],
    
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ],
    
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ],
    
    [
        [None],[None],[None],[None],[None],[None],[None],[None]
    ],   
]

## AREGLO DE PIEZAS BLANCAS

blancas= {

    "TOAB":[8,1], "CABB":[8,2], "ALCB":[8,3] ,"DAMB":[8,4],"REYB":[8,5],"ALFB":[8,6],"CAGB":[8,7],"TOHB":[8,8]       
}

## AREGLO DE PIEZAS NEGRAS
negras= {

    "TOAN":[1,1], "CABN":[1,2], "ALCN":[1,3] ,"DAMN":[1,4],"REYN":[1,5],"ALFN":[1,6],"CAGN":[1,7],"TOHN":[1,8]       
}

def piezastab(dic):
    piezas = dic.keys()
    return piezas

#### listas de claes negras y blancas
piezasblancas = piezastab(blancas)
piezasnegras = piezastab(negras)  

def tab(dic1,dic2,piez1,piez2,tablero):
    
    for e in piez1:
        pos = dic1[e]
        tablero[pos[0]-1] [pos[1]-1] = e
        
    for j in piez2:
        pos = dic2[j]
        tablero[pos[0]-1] [pos[1]-1] = j
        
    return tablero
   
    
tablero = tab(blancas,negras,piezasblancas,piezasnegras,tablero)

####bucle para el tablero
for e in tablero:
    print (e)


###  HACER LO DE MOVER EN BASE A LA CANTIDAD DE ESPACIOS Y NO A LAS COORDENADAS  ####
##     tomar la pieza que desea mover de a lista del diccionario 

def move(tablero, turno)    :
    #presentar todas las piezas disponibles
    if turno == 1:
        for e in piezasblancas:
            print(e)
        #elegir la pieza
        temp = input('Ingrese la clave de la pieza a mover ')
        target = temp.upper()
        
        if not target  in piezasblancas:
            print("La pieza ingresada no se encuentra dentro de sus piezas ")
            return move(tablero,1)
        else:
            mcant = int(input("indique la cantidad de casillas que desea moverse "))
            print("Ingrese la direccion en la que quiere moverse")
            print("1.izquierda\n2.derecha\n3.arriba\n4.abajo\n5. diagonal abajo izquierda\n6.diagonal abajo derecha\n7. diagonal arriba derecha\n.8 diagonl arriba izquierda\n")
            direc = int(input( "" ))
            
            ##bucle de movimiento
            i = 0
            w = blancas.pop(target)
            
            backup = {target:[w[0],w[1]]}
            
            tablero [w[0]-1] [w[1]-1] = [None]
            #         dic[pieza.upper()] = [x,y]
            while i < mcant:
                if direc == 1:
                    w[1] += 1
                    
                if direc == 2:
                    w[1] -= 1
                    
                    
                if direc == 3:
                    w[0] -= 1
                    
                    
                if direc == 4:
                    w[0] += 1
                    
                if direc == 5:
                    w[0] += 1
                    w[1] += 1
                    
                if direc == 6:
                    w[0] += 1
                    w[1] -= 1
                    
                    
                if direc == 7:
                    w[0] -= 1
                    w[1] += 1
                    
                    
                if direc == 8:
                    w[0] -= 1
                    w[1] -= 1
                    
                    
                if(target[0] == 'T' and direc >4):
                    print("movimiento invalido")
                    blancas.update(backup)
                    return move(tablero,1)
                
                if(target[0] == 'A' and direc <=4):
                    print("movimiento invalido")
                    blancas.update(backup)
                    return move(tablero,1)
                if(target[0] == 'R' and mcant >1):
                    print("movimiento invalido")
                    blancas.update(backup)
                    return move(tablero,1) 
                    
                    

                if ( tablero[w[0]-1] [w[1]-1] != [None]):
                    print("movimiento invalido")
                    blancas.update(backup)
                    return move(tablero,1)
                        
                i+=1
                
            if(w[0]>8):
                print("movimiento invalido")
                return move(tablero,1)
        
            if(w[1]>8):
                print("movimiento invalido")
                return move(tablero,1)
            
            
                
                
            tempdic = {target:w}
            blancas.update(tempdic)
            tablero[w[0]-1] [w[1]-1] = target
            
            print(w)
            
            for e in tablero:
                print (e)
            return move(tablero,2)
    
    elif turno == 2:
        for e in piezasnegras:
            print(e)
        #elegir la pieza
        temp = input('Ingrese la clave de la pieza a mover ')
        target = temp.upper()
        
        if not target  in piezasnegras:
            print("La pieza ingresada no se encuentra dentro de sus piezas ")
            return move(tablero,2)
        else:
            mcant = int(input("indique la cantidad de casillas que desea moverse "))
            print("Ingrese la direccion en la que quiere moverse")
            print("1.izquierda\n2.derecha\n3.arriba\n4.abajo\n5. diagonal abajo izquierda\n6.diagonal abajo derecha\n7. diagonal arriba derecha\n.8 diagonl arriba izquierda\n")
            direc = int(input( "" ))
            
            ##bucle de movimiento
            i = 0
            w = negras.pop(target)
            
            backup = {target:[w[0],w[1]]}
            
            tablero [w[0]-1] [w[1]-1] = [None]
            #         dic[pieza.upper()] = [x,y]
            while i < mcant:
                if direc == 1:
                    w[1] += 1
                    
                if direc == 2:
                    w[1] -= 1
                    
                    
                if direc == 3:
                    w[0] -= 1
                    
                    
                if direc == 4:
                    w[0] += 1
                    
                if direc == 5:
                    w[0] += 1
                    w[1] += 1
                    
                if direc == 6:
                    w[0] += 1
                    w[1] -= 1
                    
                    
                if direc == 7:
                    w[0] -= 1
                    w[1] += 1
                    
                    
                if direc == 8:
                    w[0] -= 1
                    w[1] -= 1
                    
                    
                if(target[0] == 'T' and direc >4):
                    print("movimiento invalido")
                    negras.update(backup)
                    return move(tablero,2)
                
                if(target[0] == 'A' and direc <=4):
                    print("movimiento invalido")
                    negras.update(backup)
                    return move(tablero,2)
                if(target[0] == 'R' and mcant >1):
                    print("movimiento invalido")
                    negras.update(backup)
                    return move(tablero,2) 
                    
                    

                if ( tablero[w[0]-1] [w[1]-1] != [None]):
                    print("movimiento invalido")
                    negras.update(backup)
                    return move(tablero,2)
                        
                i+=1
                
            if(w[0]>8):
                print("movimiento invalido")
                return move(tablero,2)
        
            if(w[1]>8):
                print("movimiento invalido")
                return move(tablero,2)
            
            
                
                
            tempdic = {target:w}
            blancas.update(tempdic)
            tablero[w[0]-1] [w[1]-1] = target
            
            print(w)
            
            for e in tablero:
                print (e)
            return move(tablero,1)   

##       tomar la cantidad de casillas a recorrer
##         elegir la direccion (1.x 2.y......)
##            revisar las limitaciones (bordes, piezas aliadas, piezas enemigas)
                #si existe alguna restriccion aplincar la norma de lugar
##entregar/obtener la coordenada final de la pieza
## mover la pieza a la coordenada indicada, modificando su posicion en el diccionario originak -------- llenar con un espacio en blanco 
# (none) la casilla de la que parte la pieza

### presentar el tablero con el metodo anteriormente creado
#############  si se comen las piezas, eliminarlas de la lista
#############  surrender y tablas


# def move_engranaje(claves,tablero,dic,pieza,x,y):


#     if pieza.upper() in claves:
#         w = dic.pop(pieza.upper())
#         tablero [w[0]-1] [w[1]-1] = [None]
#         dic[pieza.upper()] = [x,y]
#         tablero = tab(blancas,piezasblancas,tablero)
        
#         for e in tablero:
#             print (e)
        
#     return  

# def mover(clave,x,y):
#     move_engranaje(piezasblancas,tablero,blancas,clave,x,y)
#     return
    
    

# for e in tablero:
#     print (e)
    
    
# class pieza:
    
#     def __init__(self,x):
#         tipo_pieza = self.x
    
#     def comer(self):
#         print("comiendo")
        

# dama = pieza("dama")       
        
# dama.comer 

move(tablero,1) 
      