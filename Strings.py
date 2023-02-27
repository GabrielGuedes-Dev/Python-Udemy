''' DocString '''
# Comentário
print(12, 34, sep='', end='')
# O sep é um separador para separar os argumentos passados
# Com end vc define o que acontece no final do print, por padrão é = \n


# Escape - serve para expressões regulares
# e a barra anula o caractere seguinte
# O r serve para que as barras também apareçam
print(r'Gabriel \'Guedes\'')
# Posso usar aspas simples dentro de aspas duplas e vice-versa


A = 'Gabriel'
B = 'Guedes'
C = 'Silva'
formato = 'A: {} B: {} C: {}'.format(nome1=A, nome2=B, nome3=C)
# Se eu nomear algum parâmetro, todos que vierem após ele também deverão ser nomeados
