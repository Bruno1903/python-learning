#Generator expressions
    #Uma forma mais rapida para listas, dicionarios e etc
    #Menos memoria alocada
    #Valores em bytes
from sys import getsizeof

numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print("=========")

numeros = (x * 10 for x in range(10))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))