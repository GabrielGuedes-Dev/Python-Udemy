'''
Lambda - Funções anônimas (Sem nome), que contém apenas uma linha

No exemplo abaixo utilizamos a ordenação de uma lista e o método sorted para que possamos passar uma função como critério de ordenação, já que o python não consegue ordenar dicionários, nesse caso a função lambda é muito mais prática
'''

nomes = [
  {'Nome': 'Gabriel', 'Idade': 19},
  {'Nome': 'Isabel', 'Idade': 45},
  {'Nome': 'Mariana', 'Idade': 23}
]

nomesOrdenadosPorIdade = sorted(nomes, key = lambda nomes: nomes['Idade'])
print(nomesOrdenadosPorIdade)
