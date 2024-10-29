class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Estoy hablando")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = Empleado("Roberto",25,"Chilena","Programador",200)
print(roberto.nombre)
roberto.hablar()

