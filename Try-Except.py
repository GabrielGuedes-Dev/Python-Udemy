# Try - Tenta executar o código
# Except - Se ocorrer algum erro ele captura ele

try:
    num = int(input('Digite um número que eu lhe enviarei o dobro: '))
    print(f'O dobro de {num} é {num * 2}')
except:
    print('Isso não é um número')
