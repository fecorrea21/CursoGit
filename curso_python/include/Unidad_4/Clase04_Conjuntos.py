#Definir un conjunto
lista  = set(["Alex", 24, 1.87, True])

#Listar tabla

print(lista)

#Agregar lista
lista.add(60)

print("Lista actualizada: ", lista)

#Lista copiado
lista_copia = lista.copy()
print("Copia de lista: ", lista_copia)

#Borrar un dato
lista.remove(24)
print("Borrar campo: ", lista)

#Unir dos listas y sus diferencias

a = set([1, 2, 3, 4, 5, 6, 7])
b = set([5,6,7,8,9])

print("Unir listas: ", a.union(b))
print("Diferencias: ", a.difference(b))
