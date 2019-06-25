from include.POO.Motocicleta import *

#Objeto
moto01 = Moto("Rojo","Honda",5000000,False)
moto01.color = "Rojo"
print(moto01.color)

moto01.arrancar()
print(moto01.estado())

print("\nObjeto 02 \n===================")

#Objeto 02
moto02 = Moto("Blaca","Yamaha",4000000,False)
moto02.color = "Blanco"
print(moto02.color)

moto02.arrancar()
print(moto02.estado())
