funcionarios = {"Ana", "Marcos", "Alice", "Pedro", "Sophia", "Bruno", "Melissa"}
turno_dia = {"Ana", "Marcos", "Alice", "Melissa"}
turno_noite = {"Pedro", "Sophia", "Bruno"}
tem_carro = {"Marcos", "Alice", "Bruno", "Melissa"}

carro_noite = turno_noite.intersection(tem_carro)
print(f"Funcionarios que tem carro e trabalham a noite: \n{carro_noite}")

carro_dia = turno_dia.intersection(tem_carro)
print(f"Funcionarios que tem carro e trabalham de dia: \n{carro_dia}")

no_car = funcionarios.difference(tem_carro)
print(f"Funcionaros que nao tem carro: \n{no_car}")

#Outra alternativa:

# funcionarios = ["Ana", "Marcos", "Alice", "Pedro", "Sophia", "Bruno", "Melissa"]
# turno_dia = ["Ana", "Marcos", "Alice", "Melissa"]
# turno_noite = ["Pedro", "Sophia", "Bruno"]
# tem_carro = ["Marcos", "Alice", "Bruno", "Melissa"]
#
# lista1 = set(tem_carro).intersection(turno_noite)
# print(lista1)
#
# lista2 = set(tem_carro).intersection(turno_dia)
# print(lista2)
#
# lista3 = set(funcionarios).difference(tem_carro)
# print(lista3)