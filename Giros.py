#encodig: utf-8                                                                                                                                       
#Calcula los giros de la curva del dragon en la iteración n
def giros(n):
    'función recursiva para calcular el número de giros'
    if n ==0:
        return []
    else:
        c = giros(n-1)
        rc = c[::-1]
        i = ["I" if g == "D" else "D" for g in rc]
        return  c+["I"] + i

w = int(input("Iteración: "))
listaEntrada = []
listaSalida = []
while not w == -1:
    listaEntrada.append(w)
    w = int(input("Iteración: "))

for iteracion in listaEntrada:
    p = ""
    for giro in giros(iteracion):
        p = p+giro
    listaSalida.append(p)

print()
for x in range(0, len(listaEntrada)):
    print('Iteración ' + str(listaEntrada[x]) + ': ' + listaSalida[x] )
