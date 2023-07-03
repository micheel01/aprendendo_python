"""
CONSTANTE = varaiveis que nao vao mudar
Muitas condiçoes no mesmo if (ruim)
<- contadem de complexidade (ruim)
"""


velocidade = 61 #velocidade atual do carro
local_carro = 101 #local em que o carro esta

RADAR_1 = 60 #vel max do radar
LOCAL_1 = 100 #local onde ta o radar 1
RADAR_RANGE = 1 # a distancia do radar

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro<= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1


if vel_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

    if carro_passou_radar_1:
        print('Carro passou radar 1')

if carro_passou_radar_1 and vel_carro_passou_radar_1:
    print('carro multado radar 1')   

