def sumar(*args):
    resultado = args[0]
    for valor in args[1:]:
        resultado += valor
    return resultado

def restar(*args):
    resultado = args[0]
    for valor in args[1:]:
        resultado -= valor
    return resultado

def multiplicar(*args):
    resultado = args[0]
    for valor in args[1:]:
        resultado *= valor
    return resultado

def dividir(*args):
    resultado = args[0]
    for valor in args[1:]:
        resultado /= valor
    return resultado