# Iterando Strings com While

# nome = 'GABRIEL'

# tamanhoNome = len(nome)
# cont = 0
# nomeCopiado = ''

# while cont < tamanhoNome:
#     nomeCopiado += nome[cont]
#     cont += 1

# print(nomeCopiado)

# While/Else
# nome = 'GabrielGuedes'
# i = 0

# while i < len(nome):
#     letra = nome[i]

#     if letra == ' ':
#         break
#     print(letra)
#     i += 1

# else:  # Só é executado quando o while é executado por completo
#     print('Não encontrei espaço na string')
# print('FORA DO BLOCO')

# frase = ' O python é uma linguagem de progamação ' \
#         ' Multiparadigma ' \
#         ' Python foi criado por Guido Van Rossum'.upper()

# i = 0
# quantApareceuMaisVezes = 0
# letraApareceuMaisVezes = ''

# while i < len(frase):
#     letraAtual = frase[i]
#     if letraAtual == ' ':
#         i += 1
#         continue

#     quantLetraAtualApareceu = frase.count(letraAtual)

#     if quantLetraAtualApareceu > quantApareceuMaisVezes:
#         quantApareceuMaisVezes = quantLetraAtualApareceu
#         letraApareceuMaisVezes = letraAtual
#     i += 1

# print(letraApareceuMaisVezes, quantApareceuMaisVezes)

# Calculadora com While

while True:
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        operador = str(input('Digite a operação (+-*/): '))

        if operador.isspace() or len(operador) == 0:
            print('Por favor, digite algum operador\n')
            continue

        operadoresVálidos = '+-*/'
        if operador not in operadoresVálidos:
            print('Digite um operador válido\n')
            continue

        if len(operador) > 1:
            print('Digite apenas um operador\n')
            continue

        if operador == '+':
            resultado = num1 + num2
            print(f'\nResultado da Soma: {resultado}')
        elif operador == '-':
            resultado = num1 - num2
            print(f'\nResultado da Subtração: {resultado}')
        elif operador == '*':
            resultado = num1 * num2
            print(f'\nResultado da Multiplicação: {resultado}')
        elif operador == '/':
            resultado = num1 / num2
            print(f'\nResultado da Divisão: {resultado}')

    except:
        print('Um ou ambos número estão inválido, por favor tente novamente\n')
        continue

    sair = str(input('Deseja sair ? (S- SIM/N-NÃO): ')).upper()
    while sair.isspace() or len(sair) == 0:
        print('Valor Inválido!')
        sair = str(input('Deseja sair ? (S- SIM/N-NÃO): ')).upper()
    while sair not in 'SN':
        print('Valor Inválido!')
        sair = str(input('Deseja sair ? (S- SIM/N-NÃO): ')).upper()
    if sair == 'S':
        print('\nObrigado por utilizar nossos serviços, volte sempre!')
        break
    else:
        print()
        continue
