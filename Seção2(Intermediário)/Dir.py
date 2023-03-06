# Dir - checa os atributos do objeto, dentro do console de debugação
string = 'Gabriel'
metodo = 'upper'
# Hasattr - checa se determinado objeto tem determinado nome dentro dele
# Getattr - obtém um método dinamicamente
if hasattr(string, 'upper'):
  print('EXISTE UPPER')
  print(getattr(string, metodo)()) # Estou dizendo que a variável metodo é igual ao metodo upper
  # Esse parentese após definir a variavael como método é para chamar o método, quando falamos de tipos imutaveis fazemos desse modo direto, se retirarmos do objeto, podemos perder o objeto
else:
  print('NÃO EXISTE ESSE MÉTODO')

