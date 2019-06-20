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