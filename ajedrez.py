#################################################################

########           Que necesito hacer?            ###############
#####        tablero funcional y organizado          ###########
###       movimiento de piezas segun las reglas        #########
########          logica de comer piezas      ##################

################################################################



### Definicion de las listas que van a conformar el tablero
tablero = [
    [
        [],[],[],[],[],[],[],[]
    ],
    
    [
        [],[],[],[],[],[],[],[]
    ],
    
    [
        [],[],[],[],[],[],[],[]
    ], 
    
    [
        [],[],[],[],[],[],[],[]
    ],
    
    [
        [],[],[],[],[],[],[],[]
    ],
    
    [
        [],[],[],[],[],[],[],[]
    ],
    
    [
        [],[],[],[],[],[],[],[]
    ],
    
    [
        [],[],[],[],[],[],[],[]
    ],   
]

blancas= {

    "tab":[8,1], "cbb":[8,2], "acb":[8,3] ,"db":[8,4],"rb":[8,5],"afb":[8,6],"cgb":[8,7],"thb":[8,8]       
}

def piezastab(dic):
    piezas = dic.keys()
    return piezas

pblancas = piezastab(blancas)

def tab(dic,piezas,tablero):
    
    for e in piezas:
        pos = dic[e]
        tablero[pos[0]-1] [pos[1]-1] = e
    return tablero
   
    
tablero = tab(blancas,pblancas,tablero)


####bucle para el tablero
for e in tablero:
    print (e)
    print("a")

# print(pblancas)



# for e in tablero:
#     print (e)
    
    
# class pieza:
    
#     def __init__(self,x):
#         tipo_pieza = self.x
    
#     def comer(self):
#         print("comiendo")
        

# dama = pieza("dama")       
        
# dama.comer        