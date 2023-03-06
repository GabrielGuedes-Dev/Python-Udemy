# isinstance() Checa se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
] # Lista com vários tipos

for item in lista:
  if isinstance(item, set):
    print(item, isinstance(item, set))
    
  if isinstance(item,float): # Checa dois tipos
    print(item, isinstance(item, set))