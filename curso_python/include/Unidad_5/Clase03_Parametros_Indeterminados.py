#Inderteminados por posicion
def inderteminados(*datos_posicion):
    for datos   in datos_posicion:
        print(datos)
print("Indeterminado por posicion")
print("===========================")

inderteminados(5, "Hola MUndo", [1,2,3,4,5])

#Inderteminado por nombre
def indertemindado_nombre(**datos_nombre):
    for datos in datos_nombre:
        print(datos, "=", datos_nombre[datos])

print("Indeterminado por Nombre")
print("========================")
indertemindado_nombre(n=5, c="Hola Mundo", lista=[1,2,3,4,5])

#Inderteminado por posicion y nombre
def super_funcion(*datos_posicion, **datos_nombre):
    for datos in datos_posicion:
        print(datos)
    for datos in datos_nombre:
        print(datos, "=", datos_nombre[datos])

print("Indeterminado por nombre y posicion")
print("====================================")

super_funcion(5, "Hola", [1,2,3,4,5], n=5, c="Hola Mundo", lista=[1,2,3,4,5])
