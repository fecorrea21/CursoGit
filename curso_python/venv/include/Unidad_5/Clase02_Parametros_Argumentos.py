#Parametros y argumentos
#Funcion Sumar

def sumar(a, b, c):
    return a + b + c

resultado = sumar(4,5,6)
print("La suma es: ", resultado)

#Funcion Restar
def restar (a, b):
    return a - b

resultado = restar(b= 100, a=10)
print("La resta es: ", resultado)


#Guardar una funcion en una variable

valor = restar
print(valor(20,30))

def multiples_valores():
    return "String", 12, True

string, entero, bol = multiples_valores()
print(string, entero, bol)

def nueva_funcion(funcion):
    print(funcion(50,30))

resta = restar 
nueva_funcion(resta)