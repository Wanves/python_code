diccionario = {'Argentina': 'Buenos Aires', 'Perú': 'Limas', 'Rusia': 'Moscú'}





print(diccionario)
print(diccionario['Argentina'])
print(diccionario['Rusia'])
diccionario['Francia']='Paris'
diccionario['Argentina']='Un quilombo'
print(diccionario)

del diccionario['Rusia']
print(diccionario)

diccionario2 = {'Juan': 'Wanvestrant', 40: True}
print(diccionario2[40])

llaves = ('España','Francia','Argentina')
dicPaises = {llaves[0]:'Madrid',llaves[1]:'Paris'}
print(dicPaises)

print(dicPaises.get('España'))
print(dicPaises.keys())
print(dicPaises.values())