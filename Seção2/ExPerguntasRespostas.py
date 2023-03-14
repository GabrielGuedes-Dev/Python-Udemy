perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2 ?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 x 5 ?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },      ]

quantAcertos = 0

for pergunta in perguntas:
  for chave, valor in pergunta.items():
    if chave == 'Pergunta':
      print(chave, valor, end = '\n\n')
      
    if chave == 'Opções':
      print(chave)
      cont = 0
      for opções in valor:
        print(f'{cont}) {opções}')
        cont += 1
      opçãoUsuário = int(input('Escolha sua opção: '))
      if valor[opçãoUsuário] == pergunta['Resposta']:
        print('Acertou👍\n')
        quantAcertos += 1
      else:
        print('Errou❌\n')
  
print(f'Você acertou {quantAcertos} de 3 perguntas')