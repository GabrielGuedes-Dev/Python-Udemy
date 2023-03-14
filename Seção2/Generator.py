'''
Generator expression, Iterables e Iterators em Python
Generator - Funções que sabem pausar em determinada ocasião
Iterator - classe que tem os métodos iter e next, obrigatoriamente vamos ter que usar um iterável
Todo Generator é um Iterator, mas Iterator não é um Generator
'''
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # Tem iter e next

lista = [i for i in range(10000)]
generator = (i for i in range(10000))
# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))
# sys.getsizeof retorna o tamanho em bytes de algum valor
# O generator consome menos memória
# print(next(generator))
# Ele está parado na primeira posição, ele só avança a medida que damos next
# A lista já está toda na memória, o generator espera pedirmos um valor

# Vantagens da Lista: Como ela está toda na memória, podemos acessar valores por índice e saber seu tamanho

## Como criar uma Function Generator

# def generator (n=0, maximum = 10):
#   yield 1 # Pausa a execução da função
#   print('Continuando...')
#   yield 2
#   print('Finalizando...')
#   yield 3

# gen = generator()

# for n in gen:
#   print(n)
  
## EXEMPLO

def generator (n=0, maximum =10):
  while True:
    yield n
    
    n += 1
    if n >= maximum:
      return
  
gen = generator(n=3, maximum=9)
for n in gen:
  print(n)

# Esse tipo de função pausa no primeiro yield e retorna nele depois da pausa