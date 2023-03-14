import copy 

produtos = [
    {'Nome': 'Produto 5', 'Preço': 10.00},
    {'Nome': 'Produto 1', 'Preço': 22.32},
    {'Nome': 'Produto 3', 'Preço': 10.11},
    {'Nome': 'Produto 2', 'Preço': 105.87},
    {'Nome': 'Produto 4', 'Preço': 69.90},
           ]

novosProdutos = copy.deepcopy(produtos)
novosProdutos = [{**produto, 'Preço' : round(produto['Preço'] * 1.1, 2)} for produto in produtos] 
# round arredonda o número de acordo com a quantidade casas decimais que vc passar

produtosOrdenadosPorNome = copy.deepcopy(novosProdutos)
produtosOrdenadosPorNome = sorted(produtosOrdenadosPorNome ,key = lambda produtosOrdenadosPorNome :produtosOrdenadosPorNome['Nome'], reverse = True)

produtosOrdenadosPorPreço = copy.deepcopy(novosProdutos)
produtosOrdenadosPorPreço = sorted(produtosOrdenadosPorPreço ,key = lambda produtosOrdenadosPorPreço :produtosOrdenadosPorPreço['Preço'])

print(*novosProdutos, sep = '\n')
print()
print(*produtosOrdenadosPorNome, sep = '\n')
print()
print(*produtosOrdenadosPorPreço, sep = '\n')
