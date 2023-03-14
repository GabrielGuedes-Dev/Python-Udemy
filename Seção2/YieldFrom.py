# Yield From

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen2():
  yield from gen1() # Retoma de onde a função gen1 parou
  yield 4
  yield 5
  yield 6
  
def gen3(gen = None):
  if gen is not None:
    yield from gen() # também podemos passar a própia função como parâmetro
  yield 7
  yield 8
  yield 9