class Perro:
    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def ladrar(self):
        print(f"el perro {self.__nombre} ladra")



nahuel = Perro("Nahuel",10)
nahuel.ladrar()
print(nahuel.__dict__)