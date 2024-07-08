#Set (listas)
    #Similar a listas
    #Evita itens duplicados
    #Nao utiliza index

list = set([1,2,4,5,6]) #Set
s1 = {1,2,4,5,6} #Chaves para ser um SET
s1.add(3)
s1.update([7,8,9,10])
s1.remove(10)
s1.discard(9)


print(s1)