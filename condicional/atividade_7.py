import os
os.system('cls')

print('''
===== Mercado do senai ====
Caju R$ 2,00 por unidade''')

caju = int(input('deseja quantos caju: '))
preco = float(input('digite seu preço: '))
total = caju * preco

if caju <= 5:
    resultado = total * 0.2
elif caju > 5 and caju <= 10:
    resultado = total * 0.3
elif caju > 10:
    resultado = total * 0.5
else:
    print('opção invalida')

print(f'o seu valor foi {resultado}')



