from tutoria_clase_2.modelo import *
d = Docente("Docente B D", "Loja")
d2 = Docente("Docente Proy","Quito")
listado = [d,d2]
e = Estudiante("Luis",listado)
print(e.presentar_datos())