lista = ["Prueba", 28, 28,  1.87, True]

print(lista)

print("Cantidad de datos: ", len(lista))
lista.append("Final")
print("Cantidad: ", lista.count(28))
lista.insert(3, 1.85)
print("Ultimo valor: ", lista.pop())
lista.remove(28)
print("Lista actualizada: ", lista)

