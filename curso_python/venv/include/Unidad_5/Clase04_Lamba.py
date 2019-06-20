#Funcion Sumar
def sumar (a,b):
    return a+b

#Impresion de funcion

print(sumar(4,5))

mi_funcion = lambda a, b : a + b
revertir = lambda cadena : cadena[::-1]
mi_pregunta = lambda sentencia: '¿{}?'.format(sentencia)
no_resultado = lambda : print("Ejecutar Accion")

print(mi_funcion(10,40))
print(revertir("Hola tio"))
print(mi_pregunta("Es una pregunta"))
no_resultado()



