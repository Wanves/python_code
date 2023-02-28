


print('Prográma para saber cuantos días tiene cada mes')

diasMes = int(input(f'''
                Ingresa el mes seleccionado-> '''))

if diasMes <= 0 or diasMes >= 13:
    print('Dato ingresado incorrecto')
else:
    print('Dato ingresado correctamente')
if diasMes == 1 or diasMes == 3 or diasMes == 5 or diasMes == 7 or diasMes == 8 or diasMes == 10 or diasMes == 12:
    print(f'El mes seleccionado tiene-> 31 días')
elif diasMes == 2:
    print(f'El mes seleccionado tiene-> 29 días')
elif diasMes == 4 or diasMes == 6 or diasMes == 9 or diasMes ==11:
    print(f'El mes seleccionado tiene-> 30 días')
    
    
    
print(1)