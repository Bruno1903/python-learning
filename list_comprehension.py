#List Comprehension
    #Mais simples de se escrever
    #Utilizado qando voce precisa criar uma nova lista a partir de uma existente
    #[expressao for iten in tens]

frutas1 = ["Abacate", "banana", "Morango", "Kiwi", "Abacaxi"]
#frutas2 = []

'''for itens in frutas1:
    if "b" in itens:
        frutas2.append(itens)'''

frutas2 = [iten for iten in frutas1 if "b" in iten]

print(frutas2)

#List comprehension com numeros

#valores = []

'''for x in range(6):
    valores.append(x * 10)

print(valores)'''

valores = [x * 10 for x in range(6)]

print(valores)
