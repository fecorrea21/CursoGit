with open("C:/Users/OMNIBNK/Documents/SCRAPERS/S3/aec_20190606T19_764505832_c579ddcacd6db8841f25879b21b7b80a.xml") as a:
    contentA = set(a)

with open("C:/Users/OMNIBNK/Documents/SCRAPERS/SII/AEC34-565.xml") as b:
    contentB = set(b)

    if contentA == contentB:
        print("Los archivos son Iguales")
    elif contentA != contentB:
        print("Los archivos tienen diferencias")
    else:
        print("Fin Programa")

