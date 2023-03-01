'''
Empacotamento e Desempacotamento Básico
a, b = 1,2
a, b = b, a
'''

# Empacotamento com Dicionários
pessoa = {'Nome': 'Gabriel', 'Sobrenome': 'Guedes'}
a, b = pessoa.items() # Pode utilizar keys e values tbm
# a - chave nome e seu valor
# b - chave sobrenome e seu valor


# Desempacotamento com Dicionários
dadosPessoa  = {'Idade' : 16 ,'Altura' : 1.6}
junçãoDicionários = {**pessoa, ** dadosPessoa}

