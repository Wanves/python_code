from ast import arg
import numpy as np

class SectorGeneral:
    def __init__(self,costo,lugar):
        self.costo = costo
        self.lugar = np.zeros(lugar, Registro)
        self.ocupados = 0
    
    def __repr__(self):
        cadenaString = f"lugares:{self.costo}, {self.lugar}"
        return cadenaString
    
    def ingresar(self,placa,horaEntrada):
        self.placa = placa
        self.horaEntrada = horaEntrada
        
    def salida(self,placa,horaSalida):
        self.placa = placa
        self.horaEntrada = horaSalida
    
    def sacarRegistro(self, placa, horaSalida):
        i = 0
        for r in self.lugar:
            if r != 0 and r.placa()== placa:
                self.lugar[i] = 0
                self.ocupados -= 1
                Registro(self.lugar, i)
                return r.cuantoEstuvo(horaSalida) * self.costo
        i+=1  
      
class Registro:
    def __init__(self, placa, horaEntrada):
        self.placa = placa
        self.horaEntrada = horaEntrada

    def __repr__(self) -> str:
        cadenaString = f"({self.placa} - {self.horaEntrada})"
        return cadenaString
  
    def cuantoEstuvo(self, horaSalida):
        return horaSalida - self.horaEntrada
        
   
    

sg = SectorGeneral(10,50)
sg.ingresar('AAA111',8)
sg.ingresar('BBB222',9)
sg.ingresar('CCC333',10)
print(sg.sacarRegistro('AAA111',8))
sg.salida('AAA111',8)
sg.salida('BBB222',9)
sg.salida('CCC333',10)

sg.sacarRegistro('AAA111',8)
sg.sacarRegistro('BBB222',9)
sg.sacarRegistro('CCC333',10)

r = Registro('AAA111',8)
Registro('BBB222',9)
Registro('CCC333',10)




print(r.cuantoEstuvo(9))
print(r.cuantoEstuvo(12))
print(r.cuantoEstuvo(14))

