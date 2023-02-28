'''
Shallow Copy - Cópia usando o método copy(), faz uma cópia rasa, portanto se tivermos dados mutáveis dentro do dicionário (Listas, Dicionários) eles estarão interligados com a original

Deep Copy - Cópia usando a bibilioteca copy que tem uma função chamada deepcopy, que é uma cópia profunda
'''

# Shallow Copy
# dic1 = {'X': 2, 'Y': [1,2,3]}
# dic2 = dic1.copy()
# dic2['Y'][0] = 999 
# print(dic1)

# Deep Copy
import copy
dic1 = {'X': 2, 'Y': [1,2,3]}
dic2 = copy.deepcopy(dic1)
dic2['Y'][0] = 999 
print(dic1)