# Sets - Conjunto de dados, mutável, porém aceita apenas tipos imutáveis

# Criação de Set
# set = set() - set vazio OU
# set = {1,2,3} set com dados Chaves vazias são consideradas dicionários

# lista = [1,2,3,2,3,3,2,1,1,2,1,3]
# set = set(lista)
# print(set)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1 | set2  # União de Sets
set4 = set1 & set2  # Intersecção dos Sets
set5 = set1 - set2  # Diferença entre os sets, permanece apenas os itens da esquerda que sejam diferentes do da direita
set6 = set1 ^ set2  # Retorna itens que não estão em ambos
# print(4 in set)
# print(4 not in set)
# for numero in set:
#   print(numero)

'''
PECULIARIDADES SET

- Seus valores sempre são únicos, eles eliminam valores duplicados
- Não garantem ordem dos valores passados
- Não tem índices
- São Iteráveis (For, in ,not in)

MÉTODOS ÚTEIS EM SET

- set.add(1) Adiciona um item no set, porém só aceita um valor como parâmetro
- set.update() Também adiciona, porém de forma iterada
passar vários valores com update = set.update(('GABRIEL', 1,2,3,4,5))
- set.clear() Limpa o set
- set.discard() Elimina um item no set, passando o própio valor
'''
