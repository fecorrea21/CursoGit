#Namespace

# noinspection PyUnresolvedReferences
import modulos.matematicas
suma = modulos.matematicas.sumar (1,2,3,4,5)
print("La suma es: ", suma)

#Accediendo atraves de alias

# noinspection PyUnresolvedReferences
import modulos.matematicas as m
resta = m.restar(100,20,10)
print("La resta es: ", resta)

#Acceder a los elementos sin namesspace y alias
from modulos.matematicas import *
mult = multiplicar(2,2,2,3)
print("La multiplicacion es: ", mult)

