 
import numpy as np
# def verificar():
#     añoNacimiento = int(input('Ingresa año de nacimiento-> '))
#     edad = input('Ingresa Edad-> ')
#     nombre = input('Ingresa Nombre-> ')
#     if añoNacimiento >= 1970:
#         print('Genial eres uno de los mios')
#     elif añoNacimiento >= 1980:
#         print('Genial eres ochentoso eso es Grandioso')
#     else:
#         print('Eres de otro equipo pero es genial conocerte')
       
    
# verificar()


def datoUsuario(p,lugar,placa):
    if lugar>= len(p):
        raise Exception('No tengo lugar para esa posición')
    p[lugar]= placa 
    
c = np.zeros(5,int)
datoUsuario(c,0,777)
datoUsuario(c,1,777)
datoUsuario(c,2,777)
datoUsuario(c,3,777)
datoUsuario(c,4,777)
datoUsuario(c,5,777)
print(c)

            
