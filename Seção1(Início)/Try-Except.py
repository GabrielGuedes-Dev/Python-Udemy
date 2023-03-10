# Try - Tenta executar o código
# Except - Se ocorrer algum erro ele captura ele

try:
    num = int(input('Digite um número que eu lhe enviarei o dobro: '))
    print(f'O dobro de {num} é {num * 2}')
except Exception as error: # Conseguimos capturar qualquer exceção que ocorrer, também podemos tentar capturar erros específicos
    print(error)
else: # Caso não dê erro ele executa o else
    pass
finally: # Também sempre será executado
    pass