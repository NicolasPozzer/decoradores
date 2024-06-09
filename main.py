#Los decoradores NO MODIFICAN la funcion a la que se le decora
# solo se le asigna codigo a ejecutar antes o despues de la funcion.

def decorador(funcion):
    def funcion_modificada():
        print("Ejecutando un codigo random ANTES de la funcion...")
        funcion()
        print("Ejecutando un codigo DESPUES de la funcion...")
    return funcion_modificada

#Asinamos la anotation del decorador a utilizar
@decorador
def saludo():
    print("HOla probando funcion")

saludo()