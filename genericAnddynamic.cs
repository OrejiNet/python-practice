
persona: 
    nombre
    apellido
    edad

public habilidades 
    correr <T> (T persona):
        print(f"La persona {persona.nombre} ")

habilidades.correr<persona>()
habilidades.correr<dynamic>() # posible error 


