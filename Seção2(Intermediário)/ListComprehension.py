'''
List Comprehension é uma forma rápida de criar lista, a partir de iteráveis
'''

from pprint import pprint # Um print mais organizado

# Elemento a ser adicionador || Iteração
lista = [numero for numero in range(10)]

# Mapeamento de Dados - Pegar dados de uma lista, transforma-los (Ou não) e colocar em outra lista
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novosProdutos = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco']
                 > 20 else {**produto} for produto in produtos]  # Mapeamento com dicionários

# Utilizamos o desempacotamento para pegar todas as infos de uma vez
# No mapeamento a lista nova deve conter a mesma quantidade de elementos da lista original

# pprint(novosProdutos)

# Filtro de dados, serve para determinar os dados que vão entrar no lista do mapeamento
# lista2 = [n for n in range(10) if n < 5]
# Esquerda do for é mapeamento, direita do for é filtro

# List Comprehension com mais de um for
lista3 = [(x,y) 
          for x in range(3)
          for y in range(3)
          ]
pprint(lista3)
