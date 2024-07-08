#Tuples
    #Armazenar mais de uma informação em variaveis
    #Manter a sequencia dos dados em uma variavel
    #Nao podem ser alteradas (immultable)

cores_list = ['amarelo','verde','azul','vermelho']
cores_tuple = ('amarelo','verde','azul','vermelho') #Tuple utilizar parenteses

'''print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_tuple * 2
print(duas_listas)'''

cores_list.append('Roxo') #Aqui voce consegue alterar
print(cores_list)

cores_tuple.append('Roxo') #Aqui voce nao consegue alterar pois é uma tuple
print(cores_tuple) #tuple é imutavel