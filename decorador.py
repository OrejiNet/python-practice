class Perro:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    @property
    def nombre(self):
        print("getter")
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        print("setter")
        if nombre.strip():
            self.__nombre = nombre
        return

perro = Perro("nahuel")
perro.nombre