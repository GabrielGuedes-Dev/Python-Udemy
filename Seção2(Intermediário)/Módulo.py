'''
- O primeiro módulo executado se chama __main__
- Podemos importar um módulo inteiro ou parte dele
- Só conseguimos importar módulos na mesma pasta
- Quando importamos um módulo própio ele é singleton, ou seja, só irá importar uma vez, mesmo que você peça para ele importar várias vezes
por questões de eficiência, se quisermos importar novamente utilizamos importlib, segue o exemplo abaixo

'''
print('Este módulo se chama', __name__)

import importlib
import ExFunc as ef

for i in range(10):
  importlib.reload(ef)



