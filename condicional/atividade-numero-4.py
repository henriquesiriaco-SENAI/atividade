import os
os.system('cls')



print('''
    = = = frutas do senai = = =

Fruta  |  até 5kg       |  Acima de 5kg
morango| R$ 2,50 por Kg |  R$ 2,20 por Kg
Maçã   | R$ 1,80 por Kg |  R$ 1,50 por Kg

1 = morango  2 = maçã''')

fruta = input('maçã ou morango: ')
kilo= int(input('quantas: '))

# processamento
if fruta == 'morango' and kilo >= 5:
    preco = 2.20 * kilo
elif fruta == 'morango' and kilo <= 5:
    preco = 2.50 * kilo

elif fruta == 'maçã' and kilo >= 5:
    preco = 1.50 * kilo
elif fruta == 'maçã' and kilo <= 5:
    preco == 1.80 * kilo

else:
    print('nada a relatar')

print(f'você pediu: {fruta} e o seu preço foi {preco  }')
