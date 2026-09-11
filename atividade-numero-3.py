import os
os.system('cls')

num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

if num1 == num2:
    resultado = (f'números iguais:  {num1 + num2 }')
else:
    resultado = (f'número diferentes: {num1 * num2 }')

print(resultado)

print('=== fim do programa ===')