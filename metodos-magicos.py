class Perro:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad


    def ladrar(self):
        print(f"el perro {self.nombre} ladra")

