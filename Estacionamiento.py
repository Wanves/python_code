import numpy as np

# class Estacionamiento:
#   def __init__()
class Sector:
  def __init__(self, costo, lugares):
    self.__costo = costo
    self.__registros = np.zeros(lugares, Registro)
    self.__ocupados = 0

  def __repr__(self):
    cadenaString = f"lugares:{self.__ocupados}, {self.__registros}"
    return cadenaString

  def ingresarRegistro(self, patente, horaEntrada):
    self.__registros[self.__ocupados] = Registro(patente, horaEntrada)
    self.__ocupados += 1

  def sacarRegistro(self, patente, horaSalida):
    i = 0
    for r in self.__registros:
      if r != 0 and r.getPatente()== patente:
        self.__registros[i] = 0
        self.__ocupados -= 1
        Registro(self.__registros, i)
        return r.cuantoEstuvo(horaSalida) * self.__costo
      i+=1  


class Registro:
  
  def __init__(self, patente, horaEntrada):
    self.__patente = patente
    self.__horaEntrada = horaEntrada
  
  def __repr__(self) -> str:
    cadenaString = f"({self.__patente} - {self.__horaEntrada})"
    return cadenaString
  
  def cuantoEstuvo(self, horaSalida):
    return horaSalida - self.__horaEntrada
  
  def getPatente(self):
    return self.__patente
  
estudiantes = Sector(5, 50)
estudiantes.ingresarRegistro("aaa111", 10)
estudiantes.ingresarRegistro("aaa222", 10)
estudiantes.ingresarRegistro("bbb222", 10)
estudiantes.ingresarRegistro("ccc222", 10)
estudiantes.ingresarRegistro("ddd111", 10)

print(estudiantes)
print(estudiantes.sacarRegistro("bbb222", 13))
print(estudiantes)
estudiantes.ingresarRegistro("aaa333", 10)
print(estudiantes)

class Estacionamiento:

  def __init__(self):
    self.__es = Sector(5, 50)
    self.__pr = Sector(10, 50)
    self.__gr = Sector(20, 100)
    self.__reca = 0
  
  def ingresarAuto(self, sector, patente, horaEntrada):
    if (sector == "estudiantes"):
      self.__es.ingresarRegistro(patente, horaEntrada)
    elif (sector == 'profesores'):
      self.__pr.ingresarRegistro(patente, horaEntrada)
    elif (sector == 'general'):
      self.__gr.ingresarRegistro(patente, horaEntrada)
    else:
      raise Exception("No conozco ese sector")

  def sacarAuto(self, sector, patente, horaSalida):
    if (sector == 'estudiantes'):
      self.__reca += self.__es.sacarRegistro(patente, horaSalida)
    elif (sector == 'profesores'):
      self.__reca += self.__pr.sacarRegistro(patente, horaSalida)
    elif (sector == 'general'):
      self.__reca += self.__gr.sacarRegistro(patente, horaSalida)
    else:
      raise Exception("No conozco ese sector")

  def cuantoRecaudaste(self):
    return self.__reca

  def __repr__(self):
    return f"sector estudiantes: {self.__es}\nsector profes: {self.__pr}\nsector general: {self.__gr}n"

esta = Estacionamiento()

esta.ingresarAuto("estudiantes","aaa111", 10)
esta.ingresarAuto("estudiantes", "aaa222", 10)
esta.ingresarAuto("estudiantes", "bbb222", 10)
esta.ingresarAuto("estudiantes", "ccc222", 10)
esta.ingresarAuto("estudiantes", "ddd111", 10)

print(esta)
print(esta.sacarAuto("estudiantes","bbb222", 13))
print(esta)
esta.ingresarAuto("estudiantes", "aaa333", 10)
print(esta)
