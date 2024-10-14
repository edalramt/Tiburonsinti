#El objetivo es crear una clase Estudiante que almacene información básica 
#sobre el estudiante (nombre y calificación) y que utilice una función lambda 
#para determinar si el estudiante aprueba o no, y qué calificación obtiene.

class estudiante:
    def __init__(self,nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    
    def clasificar (self):
        nota = lambda calificacion: "Desaprobado" if calificacion < 11 else "Aprobado"
        return nota(self.calificacion)
       

estudiante1 = estudiante("Pedro", 12)
estudiante2 = estudiante("Anita", 14)
estudiante3 = estudiante("Juan", 6)

print(f"El estudiante {estudiante1.nombre} tiene de nota {estudiante1.calificacion} y ha {estudiante1.clasificar()}")
print(f"El estudiante {estudiante2.nombre} tiene de nota {estudiante2.calificacion} y ha {estudiante2.clasificar()}")
print(f"El estudiante {estudiante3.nombre} tiene de nota {estudiante3.calificacion} y ha {estudiante3.clasificar()}")




