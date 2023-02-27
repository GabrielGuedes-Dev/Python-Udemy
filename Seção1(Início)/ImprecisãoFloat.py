num1 = 0.1
num2 = 0.7
soma = num1 + num2

print(soma)
print(f'{soma:.2f}')  # Primeira forma de contornar, retorna string

# Segunda forma, segundo parâmetro é a quantidade de casas decimais que ele arredonda, retorna float
print(round(soma, 3))
