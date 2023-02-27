from random import randint
from sys import exit

cpf = ''

for i in range(0, 9):
    cpf += str(randint(0, 9))

somaDigitos = 0
cont = 10

for digito in cpf:
    somaDigitos += int(digito) * cont
    cont -= 1

calculoPrimeiroDigitoCpf = (somaDigitos * 10) % 11

if calculoPrimeiroDigitoCpf > 9:
    primeiroDigitoCpf = 0
else:
    primeiroDigitoCpf = calculoPrimeiroDigitoCpf

cpf += str(primeiroDigitoCpf)

somaDigitos = 0
cont = 11

for digito in cpf:
    somaDigitos += int(digito) * cont
    cont -= 1

calculoSegundoDigitoCpf = (somaDigitos * 10) % 11

if calculoSegundoDigitoCpf > 9:
    segundoDigitoCpf = 0
else:
    segundoDigitoCpf = calculoSegundoDigitoCpf

cpf += str(segundoDigitoCpf)

print(cpf)
