class ControlRemoto:
    def __init__(self, cantidadBotones:int = 0, marca:str = "", pilas:str = ""):
        self.cantidadBotones = cantidadBotones
        self.marca = marca
        self.pilas = pilas
        self.ancho = 0.0
        self.largo = 0.0

    def __str__(self):
        return "Control Remoto: " + self.descripcion()
    
    def descripcion(self):
        retorno = ""
        retorno = retorno + "Marca: " + str(self.marca)
        retorno = retorno + ", CantBotones:" + str(self.cantidadBotones)
        retorno = retorno + ", Pilas:" + str(self.pilas)
        retorno = retorno + ", Ancho:" + str(self.ancho)
        retorno = retorno + ", Largo:" + str(self.largo)
        
        return retorno
    


miControl = ControlRemoto(15, "BGH", "2xAAA")
#miControl.cantidadBotones = 15
#miControl.marca = "BGH"
#miControl.pilas = "2xAA"

print("Marca:", miControl.marca, "CantBotones:", miControl.cantidadBotones, "Pilas:", miControl.pilas, "Ancho", miControl.ancho, "Largo", miControl.largo)

otroControl = ControlRemoto(marca="Samsung")
otroControl.cantidadBotones = 20
#otroControl.marca = "Samsung"

print("Marca:", otroControl.marca, "CantBotones:", otroControl.cantidadBotones, "Pilas:", otroControl.pilas)

print("\nAhora uso el metodo descripcion:")
print(miControl.descripcion())
print(otroControl.descripcion())


print("\nPrint directo de la clase")
print(miControl)
print(otroControl)
