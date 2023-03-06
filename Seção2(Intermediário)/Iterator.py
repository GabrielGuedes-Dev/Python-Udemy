'''
Generator Expression
Iterables - Acessa valores sequencialmente
Iterator - Só consegue entregar o próximo valor
'''

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # Tem iter e next
print(next(iterator))
print(next(iterator))
print(next(iterator))
# Para no último valor