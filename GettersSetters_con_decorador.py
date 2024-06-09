#La utilizacion con propiedades como en este caso es mas escalable y una mejor Practica
# Utilizar este metodo de realizacion del codigo para getters y setters!
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    #Implementar Anotation @property que es propia de Python para el get
    @property
    def nombre(self):
        return self.__nombre

    #Setter de nombre
    @nombre.setter
    def nombre(self, newNombre):
        self.__nombre = newNombre

    #asignando del antes de llamar a la funcion ejecutamos este metodo de abajo para eliminar sus valores
    @nombre.deleter
    def nombre(self):
        del self.__nombre #del es para eliminar valores

objeto = Persona("Nicolas", "24")

print(objeto.nombre)

#Automaticamente se implementa el setter en Python llamando a nombre!
objeto.nombre = "Nico"
print(objeto.nombre)

#Elimina el valor que tiene nombre
del objeto.nombre

print(objeto.nombre)#Ahora daria error ya que nombre queda vacio

