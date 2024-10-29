class CellPhone():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        pass

    def llamar(self):
        print("Estas haciendo un llamado")

    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

cellPhone = CellPhone("Samsung","S32","48MP")

cellPhone.llamar()
cellPhone.cortar()

