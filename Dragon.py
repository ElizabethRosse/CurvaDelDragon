#encodig: utf-8                                                                 
#Calcula los giros de la curva del dragon en la iteración n                     

w = int(input("¿Qué iteración quieres calcular?: "))
def giros(n):
    'función recursiva para calcular el número de giros'
    if n ==0:
        return []
    else:
        c = giros(n-1)
        rc = c[::-1]
        i = ["I" if g == "D" else "D" for g in rc]
        return  c+["I"] + i

p = ""
for x in giros(w-1):
    p = p+x

print ('Giros en la iteración '+ str(w) + ': ' + str(p))
