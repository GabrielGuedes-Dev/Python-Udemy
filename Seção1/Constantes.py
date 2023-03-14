# Constantes são variáveis que não podem ser alteradas, no python existe uma convenção onde as constantes são representadas por variáveis com todas as letras em maiúsculo

# Complexidade de Código:
# - Várias condições dentro de um If
# - Quanto mais blocos de código dentro de outro pior é

velocidade = 61
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidadeCarroPassarRadar_1 = velocidade > RADAR_1
carroPassouNoRadar_1 = local_carro >= (
    LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 - RADAR_RANGE)
carroMultadoNoRadar_1 = local_carro >= (
    LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 - RADAR_RANGE) and velocidade > RADAR_1

if velocidadeCarroPassarRadar_1:
    print('Velocidade do carro passou do radar 1')

if carroMultadoNoRadar_1:
    print('CARRO MULTADO EM RADAR 1')
