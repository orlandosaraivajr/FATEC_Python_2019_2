lista1 = []
lista1 = list(range(1,10))
lista1 = lista1 + list(range(1,10))

lista2 = []
lista2 = list(range(8,15))
lista2 = lista2 + list(range(8,15))

"""
# Solução do Orlando
lista1 = set(lista1)
lista2 = set(lista2)
lista3 = list(lista1.intersection(lista2))
"""

"""
# Solução do Eduardo / Ricardo
lista3 = []
lista1 = set(lista1)
lista2 = set(lista2)

for x in lista1:
    if x in lista2:
        lista3.append(x)
print(lista3)
"""

"""
# Solução do Vinícius
lista3 = []

for item1 in lista1:
    for item2 in lista2:
        if item1 == item2:
            lista3.append(item1)
print(lista3)           
lista3 = list(set(lista3))
print(lista3)
"""

'''
# Testes do Orlando
lista = [1,2,1,2,1,"Orlando",2.4,"Saraiva",3,7,"Júnior"]

for item in lista:
    # print(item)
    if type(item) is str:
        print(item)
'''
