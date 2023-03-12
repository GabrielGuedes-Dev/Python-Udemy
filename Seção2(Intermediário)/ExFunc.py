def multiplicaPor (multiplicador):
  def multiplicandoNum (num):
    return num * multiplicador
  return multiplicandoNum

duplicar = multiplicaPor(2)
triplicar = multiplicaPor(3)
quadruplicar = multiplicaPor(4)

num = 2

print(duplicar(num))
print(triplicar(num))
print(quadruplicar(num))

print('Este módulo se chama', __name__)