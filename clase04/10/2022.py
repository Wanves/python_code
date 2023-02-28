from logging import exception, raiseExceptions
from signal import raise_signal
from xml.dom.minidom import Element
import numpy as np

# a = 2+3
# b = 4

# c = a / b

# a = 1 / b

# a = 1 / 0

# def dividi_a_x_b(a, b):
#     return a / b

# print(dividi_a_x_b(1, 2))
# print(dividi_a_x_b(10, 2))
# print(dividi_a_x_b(1, 2))

# try:
#     print(dividi_a_x_b(10, 0))
# except ZeroDivisionError as e:
#     print('b no puede ser 0')


# class Sector:
#     def __init__(self,sector,lugar):
#         sector = sector
#         lugar =np.zeros(lugar, Registro)
#         ocupados = 0
        
#     def ingresarRegistro(self, patente, horaEntrada):
#         self.__registros[self.__ocupados] = Registro(patente, horaEntrada)
#         self.__ocupados += 1

#------------------------------------------------------------------
       
def agregarSestudiante(v, i, elem):
    if i>= len(v):
        raise Exception('No tengo lugar para esa posición')
    v[i]= elem 
print('Sector Estudiantes entrada')


def sacarSEstudiante(v, i, elem):
    print('Sector Docente')
    for x in range(len(v)):
        if v[x] == 333:
            v[x] = 0
        
    

u = np.zeros(50,int)
agregarSestudiante(u,0,111222)
agregarSestudiante(u,1,222333)
agregarSestudiante(u,2,333444)
print(u)




#------------------------------------------------------------------

def sacarSDocente(v, i, elem):
    if i>= len(v):
        raise Exception('No tengo lugar para esa posición')
    v[i]= elem 
print('Sector Docente')
    
def sacarSdocente(v, i, elem):
    print('Sector Docente')
    for x in range(len(v)):
        if v[x] == 333:
            v[x] = 0
# print(sacarSestudiante)

u = np.zeros(50,int)
sacarSDocente(u,0,444555)
sacarSDocente(u,1,555666)

print(u)
sacarSdocente(u,1,555666)
print(u)

#------------------------------------------------------------------

def sacarSGeneral(v, i, elem):
    if i>= len(v):
        raise Exception('No tengo lugar para esa posición')
    v[i]= elem 
print('Sector General')
    
def sacarSgeneral(v, i, elem):
    print('Sector General')
    for x in range(len(v)):
        if v[x] == 333:
            v[x] = 0
# print(sacarSestudiante)

u = np.zeros(100,int)
sacarSGeneral(u,0,111)
sacarSGeneral(u,1,222)
sacarSGeneral(u,2,333)

print(u)
sacarSgeneral(u,4,666)
print(u)

#------------------------------------------------------------------

















#-----------------------------------------------------


# def agregarSestudiante(v, i, elem):
#     if i>= len(v):
#         raise Exception('No tengo lugar para esa posición')
#     v[i]= elem 
    
# def sacarSestudiante(v, i, elem):
#     # for j in range(len(v)):
#     #     print('No tengo lugar para esa posición')



#-----------------------------------------------------