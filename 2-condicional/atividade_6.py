import os
os.system('cls')

nome = input('Digite seu nome: ')
primeira_nota = float(input('digite sua primeira nota: '))
segunda_nota = float(input('digite sua segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if media >= 6:
    print('aprovado')
elif media >= 4.1 :
    print('recuperação')
else:
    print('reprovado')

print(f'sua media foi {media}')