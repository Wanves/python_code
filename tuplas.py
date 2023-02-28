tupla = (1,2,3,4,5,6,7,8,9,10)
tupla2 = (1,'Neo',2,'Hola Mundo',9,70,56)
tupla3 = (1,2,3,(4,5,6,7),8)
tuplaNueva = tupla2 + tupla3

a,b,c,d,e,f,g = tupla2

print(tuplaNueva)
print(f'''
      {tuplaNueva.index(3)}
      {tuplaNueva.count(2)}
      {tupla}
      {tupla2}
      {tupla3}
      {a}
      {b}
      {c}
      {d}
      {e}
      {f}
      {g}
      ''')
print(tupla2[1])
print(tupla2[-2])
print(tupla2[3:6])