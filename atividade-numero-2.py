import os
os.system('cls')

nome = input('digite seu nome: ')
genero = input('''genero M = Pasculino ou F = feminino: ''').upper()
estado_civil = input ('''Estado civil
1 - casado (a)
2 - solteiro (a)
3 - viúvo (a)
4 - divorciado (a): ''')

match genero:
    case 'M':
        print ('genero masculino')
        print (f'Nome: {nome}')

match estado_civil:
    case '1':
        print ('casado(a)')
    case '2':
        print('solteiro(a)')
    case '3':
        print('viúvo(a)')
    case '4':
        print('divorciado(a)')

    case _:
        print('opção invalida')

match genero:
    case 'F':
        print('genero feminino')
        print(f'Nome: {nome}')
if estado_civil == '1':
    tempo = int(input('quanto tempo casado  ?'))
    print(f'anos casado(a) {tempo}')




