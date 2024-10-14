#Gestión de Productos y Descuentos (sin arreglos) 
#El objetivo es crear una clase Producto que calcule el precio con descuento y 
#verifique si el descuento es válido. Se mostrarán tres productos sin usar listas o 
#arreglos. 
#Requisitos: 
#1. Crea una clase Producto con los atributos nombre, precio y descuento (en 
#porcentaje). 
#2. En el constructor de la clase Producto, crea: 
#o Un método lambda que calcule el precio con descuento. 
#o Un método lambda que verifique si el descuento es válido (el 
#descuento debe estar entre 0% y 50%). 
#3. Crea tres objetos de la clase Producto y muestra la información de cada uno 
#sin almacenarlos en una lista.

class Producto:
    def __init__(self,nombre,precio,descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
    
    
        self.precio_desc = lambda: self.precio * (1 - self.descuento / 100)
                
        self.descuento_valido = lambda: 0 <= self.descuento <= 50
        
    
    def mostrar_info(self):
        if self.descuento_valido():
            precio_final = self.precio_desc()
            print(f"Producto: {self.nombre}\nPrecio original: ${self.precio}\nDescuento: {self.descuento}%\nPrecio con descuento: ${precio_final}")
        else:
            print(f"Producto: {self.nombre}\nPrecio original: ${self.precio}\nDescuento no válido: {self.descuento}% (Debe estar entre 0% y 50%)")

 
producto1=Producto("Edgar Ramos",100,30)
producto1.mostrar_info()
producto2=Producto("Ana Lopez",53,48)
producto2.mostrar_info()
producto3=Producto("Aldair Jefferson",220,55)
producto3.mostrar_info()


