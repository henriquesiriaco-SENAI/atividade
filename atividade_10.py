import os
os.system('cls')

print('''
           ===== postinho do senai =====
Combustivel  | Quantidade Vendida | Desconto por Litro
 Álcool      | Até 25 litros      | 10%
 Álcool      | Acima de 25 litros | 20%
 Gasolina    | Até 25 litros      | 15%
 Gasolina    | Acima de 25 litros | 30% ''')

combustivel = input('\n ALCOOL OU GASOLINA?: ').upper()
quantidade = int(input('quantos litros ?'))



if combustivel == 'ALCOOL' and quantidade <= 25:
    preco = (3.79 * quantidade) * 0.10
elif combustivel == 'ALCOOL' and quantidade >= 25:
    preco =  (3.79 * quantidade) * 0.20

elif combustivel == 'GASOLINA' and quantidade <= 25:
    preco = (6.59 * quantidade) * 0.15
elif combustivel == 'GASOLINA' and quantidade  >= 25:
    preco = (6.59 * quantidade) * 0.30

else:
    print ('Nada a relatar')

print(f'você pediu: {combustivel} e o seu preço foi {preco}')


