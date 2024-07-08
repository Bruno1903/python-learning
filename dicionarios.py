#Dicionarios
    #Utiliza index no formato de Keys e Values
    #Aceita string, integer, float, boolena


aluno = {
    "nome": "Ana",#Key #Value
    "idade": 16,
    "nota_final": "A",
    "Aprovacao": True,
    "Materias": ["Fisica", "Matematica", "Ingles"]
}

"""print(aluno)
print(aluno["nome"])

aluno["nome"] = "Jose"

aluno.update({"nome": "Juan", "nota_final": "B"})
print(aluno)

aluno.update({"endereco": "Rua A"})
print(aluno)

print(aluno.get("endereco", "Nao existe")) #Se nao existir ele print o "Nao existe"

del aluno["idade"]
print(aluno)
"""

#For loop em dicionarios
"""for keys, values in aluno.items():
    print(keys, values)

for x in aluno.items():
    print(x)"""

print(aluno)
print(aluno.get("Materias"))
print(len(aluno))
print(aluno.keys())
print(aluno.items())
print(aluno.values())