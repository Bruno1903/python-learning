#Set (listas)
    #Similar a listas
    #Evita itens duplicados
    #Nao utiliza index

list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)#UNION  #Printa as listas sem repetir os valores
print(num1 - num2)#DIFFERENCE
print(num1 ^ num2)#Symmetric difference #Retira os duplicados nas duas listas
print(num1 & num2)#AND #mostra os dusplicados entre as duas listas
print(len(num1))
print(num1[0]) #Nao da certo pois perde a indexacao