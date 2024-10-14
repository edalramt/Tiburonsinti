#2. Un concesionario tiene 3 vehículos que tienen los atributos marca, modelo y 
#precio. La concesionaria requiere : 
#• Un método para agregar vehículos a una lista 
#• Un método para mostrar los vehículos almacenados en la lista. 
#Realizar el ejercicio usando la colaboración de clases. 

class vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca 
        self.modelo = modelo 
        self.precio = precio
        
    def imprimir(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nPrecio: {self.precio}")

class Concesionario:
    def __init__(self):
        self.vehiculos = []
 
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.marca} - {vehiculo.modelo} agregado.")

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos en el concesionario.")
        else:
            print("Vehículos en el concesionario:")
            for vehiculo in self.vehiculos:
                vehiculo.imprimir() 

car1 = vehiculo("Toyota", "MR2", 25000)
car2 = vehiculo("Hyundai", "i30 Fastback", 24640)
car3 = vehiculo("Chevrolet", "Camaro SS", 59990)


concesionario = Concesionario()


concesionario.agregar_vehiculo(car1)
concesionario.agregar_vehiculo(car2)
concesionario.agregar_vehiculo(car3)

concesionario.mostrar_vehiculos()
