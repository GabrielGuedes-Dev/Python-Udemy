# def soma(x, y, z=None):  # Z tem um valor padrão None, que será utilizado se seu valor não for passado nos argumentos, se vc nomear um parâmetro, todos após ele tem que ter um valor padrão também
#     if z is not None:
#         print(x, y, z, x+y+z)
#     else:
#         print(x, y, x+y)


# def calculadoraSoma(*args):  # Na hora da chamada da função posso botar quantas quiser
#     somatória = sum(args)
#     return somatória


# soma = calculadoraSoma(2, 2, 2, 2, 2)
# print(soma)

# EXERCÍCIO 1

# def mult(*valores):
#     multiplicação = 1
#     for valor in valores:
#         multiplicação *= valor
#     return multiplicação


# multiplica = mult(2, 2, 2, 2, 2)
# print(multiplica)

def parImpar(num):
    if num % 2 == 0:
        return "PAR"
    return "ÍMPAR"


numero = 11
print(f'O número {numero} é {parImpar(numero)}')
