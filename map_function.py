#Map function
    #Muito utilizado com listas
    #Aplicar uma funcao a um Iterable (lista), por item. (list, tuple, dic etc.)

'''lista1 = [1,2,3,4]

def multi(x):
    return x * 2

print(multi(2))

lista2 = map(multi, lista1)

print(list(lista2))'''


#Funcao map com lambda:

lista1 = [1,2,3,4]

'''def multi(x):
    return x * 2'''


#lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))

