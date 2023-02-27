# Closure são funções que retornam outras funções

def criarSaudação (saudação): # Função Closure
  def saudar(nome):
    return f'{saudação}, {nome}!'
  return saudar

falarBomdia = criarSaudação('Bom dia') # Essa variável armazena a função retornada pela fução Closure
nomes = ['Gabriel', 'Isabel', 'Mariana']

for nome in nomes:
  print(falarBomdia(nome))
  
# Conseguimos dinamizar a criação dessas saudações com nomes diferentes, que sem esse recurso ficaria mais complicada
  