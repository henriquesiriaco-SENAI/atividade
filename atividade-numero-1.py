import os
os.system('cls')

num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
num3 = int(input('digite o terceiro numeor: '))

juntos = num1 + num2

if juntos > num3:
    print(f'o primeiro e segundo numeros são maiores que o terceiro: {num1 , num2}  juntos: {juntos} o terceiro :{num3}')
else:
    print(f'o terceiro numero ainda é maior que o primeiro e terceiro, numeros:{num1 , num2} juntos: {juntos} o terceiro {num3}')

print('==== fim do programa ====')