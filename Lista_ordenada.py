list=input("introduzca numeros separados por coma:")
lista=list.split(",")
print(lista)
for a in range(len(lista)):
    lista[a]=int(lista[a])
print(lista)
d=len(lista)-1
for b in range(len(lista)):
    for c in range(len(lista)-1):
        aux=lista[c]
        if lista[c]>lista[c+1]:
            lista[c]=lista[c+1]
            lista[c+1]=aux
print(lista)