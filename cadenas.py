texto = 'Simple es mejor que complejo'


print(texto)
print(texto.strip())
print(texto.lower())
print(texto.upper())
print(texto.title())

print(texto.find('que'))

print(texto.count('e'))
a = texto.replace('e', '*')
print(a)

texto1 = texto.split(' ')
print(texto1)
print(len(texto1))