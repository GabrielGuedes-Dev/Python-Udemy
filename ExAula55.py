"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# try:
#     numInteiro = int(input('Digite um número inteiro: '))

#     par = numInteiro % 2 == 0

#     if par:
#         print('Este número é par')
#     else:
#         print('Este número é ímpar')

# except:
#     print('Este não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# try:
#     horario = int(input('Digite a hora: '))

#     dia = 0 <= horario <= 11
#     tarde = 12 <= horario <= 17
#     noite = 18 <= horario <= 23

#     if dia:
#         print('Bom dia!')
#     elif tarde:
#         print('Boa Tarde!')
#     elif noite:
#         print('Boa noite!')
#     else:
#       print('Isto não é um horário')

# except:
#     print('Digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiroNome = input('Digite seu primeiro nome: ').strip()

tamanhoNome = len(primeiroNome)
curto = tamanhoNome <= 4
normal = 4 < tamanhoNome < 7
grande = tamanhoNome > 6
num = primeiroNome.isdigit()

if tamanhoNome > 2:

    if num:
        print('Por favor, digite um nome!')
    elif curto:
        print('Seu nome é curto')
    elif normal:
        print('Seu nome é normal')
    elif grande:
        print('Seu nome é muito grande')
else:
    print('Digite um nome com pelo menos 3 letras')
