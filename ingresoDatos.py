
# nombre = input('Ingrese su nombre-> ')
# edad = input('Ingrese su edad-> ')
# print(f'Hola {nombre}, tu edad es-> {edad}')





# operacion = 0
# operacion += 20
# operacion += 30
    
# print(operacion,end=' ')
# operacion = 0
# limite = 10
# while operacion <= limite:
#     operacion +=1
    
#     print(f'Vuelta-> {operacion}')
#     print('Genial')
#     print('--------')
vlHora = 10
print(f'Valor por hora-> {vlHora}')
horaEntrada = int(input('Hora de entrada-> '))
horaSalida = int(input('Hora de Salida-> '))
vlTotal = 0
limite = 5
vlTotal = vlHora*(horaSalida-horaEntrada)


print(f'Total a abonar->{vlTotal}')