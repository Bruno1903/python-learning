#WHILE
#Excelente para loops dependentes de uma condicao
#Publiar um produto com comissao de 10% se for acima de R$20

valor = int(input("Digite o valor do seu produto: "))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f"O valor final do seu produto será de R${valor}")
    break


'''#Ternary operators
idade = 16
if idade >= 16:
    resultado = print("Voto permitido")
else:
    resultado = print("Voto nao permitido")

resultado = "Voto permitido" if idade >= 16 else "Voto nao permitido"

print(resultado)

'''
'''# WHILE

valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f" No dia {dia} o produto vai ser vendido por R${valor}")
    valor -= 5
'''


'''# for loop nested
#for numero1 in range(5):
#    print(numero1)
#    for numero2 in range(5):
#        print(numero2)

#palavra = "FANTASTICO"
#for espaco in palavra:
#    print(f"{espaco} ", end="")

linhas = 6
colunas = 6
simbolo = "@"

for i in range(linhas):
    for j in range(colunas):
        print(simbolo, end="")
    print()
'''

'''# FOR loops

#for i in range(1,6):
#    print(i)
#palavra = 'Google'

#for i in palavra:
#    print(f"{i} Esta dentro da palavra {palavra}")

compra_confirmada = False
dados_compra = "Compra no valor de R$12,50 e entrega confirmada"

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviados para o seu email")
        break
    else:
        print("Falha na compra")

'''

'''#Multiple comparison operators

valor = 10

if 20 <= valor < 40: #if valor >= 20 and valor < 40:
    print("Produto aceito")
else:
    print("Produto negado")
'''


'''#Logical operators

renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print("Financiamento aprovado")
else:
    print("Financiamento negado")
'''

'''#Assignment operators

x = 10
x = x + 5
x += 5
x -= 5
x *= 5
x /= 5
x %= 5
'''

'''mensagem = "Eu adoro comida caseira"

print(mensagem.upper()) #Metodos
print(mensagem.find('c'))
print(mensagem.replace("caseira",'feita em casa'))
'''

'''nome= 'Marcos'
sobrenome = 'Silva'
profissao = 'programador'

texto = f"O {nome} {sobrenome} e um excelente [{profissao}]"
print(texto)
'''
# O Marcos Silva e um excelente [programador]


'''valor = 99.75
valor = str(valor)
#index  01234
print(valor[3:5])
'''

'''ano_nascimento = input("Em que ano voce nasceu: ")
print(type(ano_nascimento))
idade = 2020 - ano_nascimento
print(type(idade))'''

'''nome = input('Qual é o seu nome: ')
idade = input("Qual é a sua idade: ")
idade = str(idade)
cidade = input("Onde voce mora: ")

print("O " + nome + " tem " + idade + " anos de idade e mora em " + cidade + ".")
'''

#O Andre tem 32 anos de idade e mora na cidade de Sao Paulo.