class Estudiante:
    def __init__(self, nombre, edad, grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'el estudiante {self.nombre} está estudiando')


nombre = input("Ingresa tu nombre: \n")
edad   = input("Ingresa tu edad: \n")
grado  = input("Ingresa tu grado: \n")

cristopher = Estudiante("Cristopher",edad,grado)
cristopher.estudiar()