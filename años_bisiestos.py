inicio = int(input("Ingrese el año de inicio: "))
fin = int(input("Ingrese el año de fin: "))

años_bisiestos = []
for año in range(inicio, fin + 1):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        años_bisiestos.append(año)

print("Años bisiestos en el rango {}: {}".format((inicio, fin), años_bisiestos))
