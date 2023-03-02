# Kwargs, utilizamos dois *
# Retorna um dicionário
# Com isso podemos nomear os argumentos, que serão chave e valor do dicionário

# Se quisermos argumentos não nomeados, usamos args no parâmetro

def mostraArgsNomeados (**kwargs): # Empacotamos os valores no dicionário kwargs
  for chave, valor in kwargs.items():
    print(chave, valor)
    
mostraArgsNomeados(Nome= 'Gabriel', Idade= 19)

# Utilizando a função para desempacotar um dicionário

configurações = {'Arg1': 1,'Arg2': 2,'Arg3': 3,'Arg4': 4}
mostraArgsNomeados(**configurações) # Desempacotando