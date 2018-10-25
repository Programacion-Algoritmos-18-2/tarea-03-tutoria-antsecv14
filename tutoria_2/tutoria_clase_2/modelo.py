class Docente:
	def __init__(self,n,a):
		self.nombres = n
		self.ciudad = a
	def agregar_nombres(self,n):
		self.nombres = n
	def agregar_ciudad(self,a):
		self.ciudad = a
	def obtener_nombres(self):
		return self.nombres
	def obtener_ciudad(self):
		return self.ciudad
	def presentar_datos(self):
		cadena = "%s\n\t%s"%(self.obtener_nombres(),self.obtener_ciudad())
		return cadena
class Estudiante:
	def __init__(self,n,lista_docentes):
	    self.nombres = n
	    self.docentes = lista_docentes
	def agregar_nombres(self,n):
		self.nombres = n
	def agregar_lista(self,lista_docentes):
		self.docentes = lista_docentes
	def obtener_nombres(self):
		return self.nombres
	def obtener_lista(self):
		return self.docentes
	def presentar_datos(self):
	    cadena = "Estudiante : %s\n"%(self.obtener_nombres())
	    cadena = "%s  %s\n"%(cadena,"lista Docentes")
	    for x in range(0, len(self.docentes)):
	    	cadena = "%s\n\t-%s %s" %(cadena,self.docentes[x].obtener_nombres(),self.docentes[x].obtener_ciudad())
	    return cadena