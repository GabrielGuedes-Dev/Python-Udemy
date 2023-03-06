# Muito parecido com list comprehension

produto = {
    'Nome': 'Caneta',
    'Preço': 2.5,
    'Categoria': 'Escritório'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

# print(dc)

# Conversão de Lista em Dicionário
lista = [
    ('Nome', 'Gabriel'),
    ('Idade', 19)
]

lista2 = dict(lista)
# print(lista2)

# Set Comprehension

set = {i ** 2 for i in range(10)}
print(set)
