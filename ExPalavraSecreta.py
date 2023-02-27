import os

palavraSecreta = list('BOTAFOGO')
palavraEmAsterisco = list('********')

titulo = "JOGO DA ADIVINHAÇÃO"
print(f'{titulo:^50}')

quantidadeTentativas = 0

try:
    while True:
        tentativa = str(input('\nDigite uma letra: ')).upper()
        quantidadeTentativas += 1

        tamanhoTentativa = len(tentativa)
        tamanhoIgualAzero = tamanhoTentativa == 0
        apenasEspaços = tentativa.isspace()
        apenasNumeros = tentativa.isdigit()
        tamanhoMaiorQueUmaLetra = tamanhoTentativa > 1

        if tamanhoIgualAzero or apenasEspaços or apenasNumeros:
            print('Por favor, digite uma letra!')
            continue

        if tamanhoMaiorQueUmaLetra:
            print('Digite apenas uma letra')
            continue

        for letra in palavraSecreta:
            if letra == tentativa:
                posiçãoLetra = palavraSecreta.index(tentativa)
                palavraSecreta[posiçãoLetra] = "-"
                palavraEmAsterisco[posiçãoLetra] = tentativa

        if "*" not in palavraEmAsterisco:
            os.system('clear')
            print('\nPARABÉNS, VOCÊ GANHOU!!')
            print('A palavra era: ', end='')
            for letra in palavraEmAsterisco:
                print(letra, end='')
            print(f'\nQuantidade de Tentativas: {quantidadeTentativas}')
            break

        for letra in palavraEmAsterisco:
            print(letra, end='')


except:
    print('Valor inválido, digite uma letra')


'''
Outro método de fazer era criando uma variável que armazenaria as letras que o usuário fosse acertando, e na hora de exibir a palavra se a letra estivesse nessa variável era printada, se não tivesse printava asterisco
'''
