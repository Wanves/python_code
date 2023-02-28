
# contador = 0
# while contador < 50:
#     contador += 1 
#     print('*',end=' ')
    
# altura = 10
# for i in range(altura):
#     for j in range(i+1):
#         print('*',end=' ')
#     print('       ''q')
    
    






# num = int(input('Ingrese número-> '))
# numeroSecreto = 7

# contadorIntentos = 0

# while num != numeroSecreto:
#     contadorIntentos = contadorIntentos + 1
#     print('No es el número, vueve a intentar')
#     num = int(input('El número-> '))
#     if contadorIntentos == 5:
#         break
        
# if contadorIntentos == 5:        
#     print('Tus intentos han llegado al máximo') 
# else:
#     print('Genial has adivinado el número secreto') 
#     print(f'Has intentado {contadorIntentos} veces')  

# suma = 0
# suma = suma + (1 + 8)
# suma = suma + (2 + 9)
# suma = suma + (3 + 10)
# suma = suma + (7 + 20)

# print(suma)
n = input('Ingrese su edad-> ')
mayoresEdad = 0
menoresEdad = 0
sumaEdad = 0
promedio = 0
cont = 1

while cont >= n:
    print('Edad-> ',cont,':')
    edad = input()
    
    if edad >= 18:
        mayoresEdad = mayoresEdad + 1
    else:
        menoresEdad = menoresEdad + 1
        
    sumaEdad = sumaEdad + edad
    
    cont = cont + 1
    
promedio = sumaEdad / n

print('Menores-> ',menoresEdad)
print('Mayores-> ',mayoresEdad)
print('Sumas-> ',sumaEdad)
print('Promedio-> ',promedio)
    
