#Factorial de un numero
#===========================

def factorial_numero(numero):

    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


resultado1 = factorial_numero(4)
print(resultado1)

resultado2 = factorial_numero(5)
print(resultado2)