lista = [1,2,3,'perro','jirafa','mundo']


lista.append('Genial')

lista.insert(5,'Goku')
lista.extend(['Python','Java','JavaScript'])




print(f'''
      {lista}
      {lista[:]}
      {lista[4]}
      {lista[-2]}
      {lista[2:5]}
      {lista}
      {lista.index('Python')}
      {lista.remove('Java')}
      {lista.pop()}
      {lista * 2}
      ''')
print('Python' in lista)
