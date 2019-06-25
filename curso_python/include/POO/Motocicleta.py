class Moto():

    def __init__(self, color, marca, precio, en_marcha):
        self.color = color
        self.marca = marca
        self.precio = precio
        self.en_marcha = en_marcha

    def arrancar(self):
        self.en_marcha = True
    def girar(self):
        pass


    def frenar(self):
        pass

    def estado(self):
        if self.en_marcha:
            print("Moto en movimiento")
        else:
            print("Moto esta detenida")