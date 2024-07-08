#Listas
    #Armazenas mais de uma informacao em variaveis
'''
cidades = ['Rio de janeiro', 'Sao Paulo', 'Salvador', 'Goaiania']

#https://docs.python.org/3/tutorial/datastructures.html
#cidades[0] = 'Brasilia'
#print(cidades[0])
#cidades.append('Santa Catarina')
#cidades.remove('Salvador')
#cidades.insert(1,'Santa Catarina')
#cidades.pop(0)
cidades.sort()
print(cidades)
'''

'''
#Concatenando listas

numeros = [2,3,4,5,]
letras = ['a', 'b', 'c', 'd']

final = numeros + letras
#print(final)

numeros.extend(letras)
#print(numeros)

itens = [['item2', 'item2'], ['item3', 'item4']]
print(itens[1][1])
'''
'''
#Unpacking lists
    #Armazenar mais de uma informacao em variaveis

produtos = ['arroz', 'feijao', 'laranja', 'banana',]

item1, item2, item3, *outros = produtos

''''''item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]''''''

print(item1)
print(item2)
print(item3)
print(outros)
'''

'''
#For na lista [vetor]
valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f'O valor final do produto é de R$ {x}.')
'''

'''
cor_cliente = input("Digite a cor desejada: ")
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Nao temos esta cor em estoque')

'''
'''
#Agregando duas listas com *ZIP*
cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10,20,30,40]

duas_listas = zip(cores, valores)
print(list(duas_listas))

var = list('comprar')
print(var)
'''
'''
#Criar uma lista a partir do input do usuario

frutas_usuario = input("Digite o nome das frutas seeparados por virgula: ")

frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)
'''