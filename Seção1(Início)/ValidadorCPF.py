import re  # Expressões Regulares
from sys import exit

try:
    while True:
        cpf = str(input('Digite o CPF: '))
        cpf = re.sub(r'[^0-9]', '', cpf)
        # 1º Parâmetro: Expressção regular - Substituir tudo que não estiver entre 0 e 9
        # 2º Parâmetro: O que quero susbtituir no lugar
        # 3º Parâmetro: a string

        # Repetição de Caracteres Iguais
        primerioCaractere = cpf[0]
        cpfDigitosRepetidos = primerioCaractere * len(cpf)
        if cpf == cpfDigitosRepetidos:
            print('CPF INVÁLIDO')
            exit()

        tamanhoCpf = len(cpf)
        tamanhoIgualAzero = tamanhoCpf == 0
        apenasEspaços = cpf.isspace()
        tamanhoEspecifico = tamanhoCpf == 11

        if tamanhoIgualAzero or apenasEspaços:
            print('Por favor, digite um cpf\n')
            continue

        if not tamanhoEspecifico:
            print('Valor de cpf inválido, digite novamente\n')
            continue

        noveDigitos = cpf[:9]
        dezDigitos = cpf[:10]

        somaDigitos = 0
        cont = 10

        for digito in noveDigitos:
            somaDigitos += int(digito) * cont
            cont -= 1

        calculoPrimeiroDigitoCpf = (somaDigitos * 10) % 11

        if calculoPrimeiroDigitoCpf > 9:
            primeiroDigitoCpf = 0
        else:
            primeiroDigitoCpf = calculoPrimeiroDigitoCpf

        somaDigitos = 0
        cont = 11

        for digito in dezDigitos:
            somaDigitos += int(digito) * cont
            cont -= 1

        calculoSegundoDigitoCpf = (somaDigitos * 10) % 11

        if calculoSegundoDigitoCpf > 9:
            segundoDigitoCpf = 0
        else:
            segundoDigitoCpf = calculoSegundoDigitoCpf

        verificaçãoPrimeiroDigito = primeiroDigitoCpf == int(cpf[9:10])
        verificaçãoSegundoDigito = segundoDigitoCpf == int(cpf[10:11])

        if verificaçãoPrimeiroDigito and verificaçãoSegundoDigito:
            print('CPF VALIDADO')
            break
        else:
            print('CPF INVÁLIDO')
            break


except Exception as erro:
    print(erro)
    print('Valor de cpf inválido, digite novamente')
