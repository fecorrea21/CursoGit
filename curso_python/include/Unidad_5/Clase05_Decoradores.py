def decorador (funcion):
    def nueva_funcion (*args, **kwargs):
        print("Ejecutando funcion")
        funcion(*args, **kwargs)
        print("Fin de la ejecucion")
    return nueva_funcion

@decorador
def saluda ():
    print("Hola mundo")

@decorador
def sumar (a,b):
    print("La suma es: ", a+b)


saluda()
sumar(23,456)

#Docstring

print("====================================================================0")

def saluda():
    """Esta funcion saluda"""
    saluda = "Hola mundo"
    return saluda

print(saluda)

def generadores(*args):
    for valor in args:
        yield valor*10
        print("Despues del yield")

for valor in generadores(1,2,3,4,5,6,7):
    print(valor)


doc = saluda.__doc__
nombre = saluda.__name__
print(doc,nombre)