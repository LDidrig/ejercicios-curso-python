def espacios_libre(hilera):
    inicio = 0
    inicio_max = 0
    espacio = 0
    espacio_max = 0
    hilera = hilera.lower()
    for i in range(len(hilera)):
        if hilera[i] == 'x':
            if espacio > espacio_max:
                espacio_max = espacio
                inicio_max = inicio
                espacio = 0
                inicio = 0
        else:
            espacio += 1
            if espacio == 1:
                inicio = i
    if inicio_max == 0:
        espacio_max -= 1
    else:
        if (espacio_max%2==0):
            espacio_max = int((espacio_max/2)-1)
        else:
            espacio_max = int(espacio_max//2)
    return espacio_max

camas = str(input())
vector = [int(0)]*100
f = 0
while camas!='':
    camas_libres = espacios_libre(camas)
    vector[f] = camas_libres
    f += 1
    camas = str(input())
for k in range(f):
    print(vector[k])
