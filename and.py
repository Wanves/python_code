
nombreUsuario = input('Ingresa usuario-> ')
contraseña = input('Contraseña usuario-> ')

nombreUsuario2 = input('Ingresa usuario-> ')
contraseña2 = input('Contraseña usuario-> ')

nombreUsuario3 = input('Ingresa usuario-> ')
contraseña3 = input('Contraseña usuario-> ')


if nombreUsuario == 'Wanves72' and contraseña == 'zoe72':
    print('Has ingresado, Bienvenido')
else:
    print('Contraseña usuario Incorrecta')
    
if nombreUsuario2 == 'goku' and contraseña2 == '123namek':
    print('Has ingresado, Bienvenido')
else:
    print('Contraseña usuario Incorrecta')
    
if nombreUsuario3 == 'neo' and contraseña3 == 'matrix777':
    print('Has ingresado, Bienvenido')
else:
    print('Contraseña usuario Incorrecta')        
    
datoUsuario= [nombreUsuario + contraseña]
datoUsuario2=[nombreUsuario2 + contraseña2]
datoUsuario3=[nombreUsuario3 + contraseña3]
hiperDatosUsuarios = datoUsuario + datoUsuario2 + datoUsuario3

print(f'''
      [datoUsuario]
      [datoUsuario2]
      [datoUsuario3]
      ''')
print(hiperDatosUsuarios)

