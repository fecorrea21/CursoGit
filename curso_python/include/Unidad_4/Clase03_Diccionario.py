#Definir un diccionario

lista = { 'Clave1' : "Alex",
          'Clave2' : 24,
          'Clave3' : 1.87,
          'Clave4' : True}

#Listar Diccionario

print(lista)

#Modificar datos del diccionario
lista['Clave4'] = False

#Agregar datos
lista['Clave5'] = True

#obtener un valor de acuerdo a su  clave
print("El valor es: ", lista['Clave1'])
print("Lista actualizada", lista)

#Copiar tabla

otra_lista = lista.copy()
print("Otra lista: ", otra_lista)

#Obtener valor con get
print("Valor con Get: ", lista.get('Clave3'))

#lIsta de claves
print("Lista de datos: ", lista.values())

#Borrar datos
lista.clear()

