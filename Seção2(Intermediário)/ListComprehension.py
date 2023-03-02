'''
List Comprehension é uma forma rápida de criar lista, a partir de iteráveis
'''

# Elemento a ser adicionador || Iteração
lista = [numero for numero in range(10)]

# Mapeamento de Dados - Pegar dados de uma lista, transforma-los (Ou não) e colocar em outra lista
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
           ]

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos] # Mapeamento com dicionários

# Utilizamos o desempacotamento para pegar todas as infos de uma vez
# No mapeamento a lista nova deve conter a mesma quantidade de elementos da lista original

print(*novos_produtos, sep='\n') 