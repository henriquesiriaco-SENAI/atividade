import os
os.system('cls')

print('''
==== CDS ====

VERDE    | R$ 10,00
 AZUL    | R$ 20,00
AMARELO  | R$ 30,00
VERMELHO | R$ 40,00''')

cor = input('qual cor você deseja ?:  ').upper()

match cor:
    case 'VERDE':
        print('valor R$ 10,00')
    case 'AZUL':
        print('valor 20,00')
    case 'AMARELO':
        print('valor 30,00')
    case 'VERMELHO':
        print('valor 40,00')

    case _:
        print('opção invalida')