#Funcion recursiva

def cuenta_regresiva(numero):
    numero -=1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Prueba")
    print("Fin funcion", numero)

cuenta_regresiva(5)

#Funcion recursiva con return

def factorial(numero):
    print("Valor inicial", numero)
    if numero > 1:
        numero = numero * factorial(numero-1)
    return numero

print(factorial(5))

print("=================================================0")
#yield

def saluda ():
    """Esta funcion dice hola """
    saluda = "Hola que tal"
    return saluda
    print("Otro saludo")

print(saluda ())

def generadores (*args):
    for valor in args:
        yield valor*10
        print("Despues de yield")

for valor in  generadores(1,2,3,4,5,6):
    print(valor)

doc = saluda.__doc__
nombre = saluda.__name__
print(doc, nombre)
