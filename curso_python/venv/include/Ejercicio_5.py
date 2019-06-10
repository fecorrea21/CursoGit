while True:
    print("Por favor eliga una opcion: ")
    print("1) Ingresar Datos \n2) Salir ")

    opcion = input("Ingrese")

    if opcion == '1':

        nombre = input("Ingrese su nombre")
        print("1)Hombre  2)Mujer")
        genero = input("Seleccione")

        if genero == '1':
            print("Hola", nombre,"Su genero es: ")
        elif genero == '2':
            print("Hola",nombre,"Su genero es: ")
        else:
            print("")

    elif opcion == '2':
        print("Cerrar programa")
        break
    else:
        print("Opcion incorrecta")
