

#lista = []
#print(dir(lista)) #extrae nombres de atributos y metodos de un objeto

class Tarjeta:
    def __init__(self, _titular, _numero, _vencimiento, _codigoSeguridad):
        self.titular = _titular
        self.numero = int(_numero)
        self.vemcimiemto = _vencimiento
        self.codigoSeguridad = int(_codigoSeguridad)
        self.activa = False
        self.saldo = 0.0
        self.limite = 0.0
        self.consumos = []
    
    def __str__(self):
        return f"TC Nro:{self.numero} Nombre: {self.titular} Activada: {self.activa} Limite: {self.limite} saldo: {self.saldo}" 

    def activarTarjeta(self, limiteActual):
        self.activa = True
        self.limite = limiteActual
        self.saldo = self.limite
    
    def agregarConsumo(self, detalle, Importe):
        if (self.saldo < Importe):
            print("Saldo insuficiente.")
            return False

        self.saldo = self.saldo - Importe

        self.consumos.append({"detalle": detalle, "importe":Importe})
        return True

    def verConsumos(self):
        print("Consumos del mes:")
        for consumo in self.consumos:
            print(consumo["detalle"], - consumo["importe"])
    
    def pagarTarjeta(self, importe):
        self.saldo = self.saldo + importe
        self.consumos.append({"detalle": "Pago de Tarjeta", "importe": - importe})







miTarjeta = Tarjeta("Diego Penna", 4500000122223333, "2026-06-06", 123 )
print(miTarjeta)
miTarjeta.activarTarjeta(100000)
print(miTarjeta)

if (miTarjeta.agregarConsumo("Carrefoour Express", 80000)):
    print("Transaccion exitosa")
else:
    print("Ocurrio un Error al realizar el pago")

print(miTarjeta)
miTarjeta.verConsumos()


if (miTarjeta.agregarConsumo("Dia", 15000)):
    print("Transaccion exitosa")
else:
    print("Ocurrio un Error al realizar el pago")


print(miTarjeta)
miTarjeta.verConsumos()

print("Pago la tarjeta 30000")
miTarjeta.pagarTarjeta(30000)

print(miTarjeta)
miTarjeta.verConsumos()

print("Pago la tarjeta 100000")
miTarjeta.pagarTarjeta(100000)


print(miTarjeta)
miTarjeta.verConsumos()



print(Tarjeta)