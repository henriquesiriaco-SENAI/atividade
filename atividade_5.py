import os
os.system('cls')

primeiro_numero = int(input('Digite seu primeiro número: '))
segundo_numero = int(input('Digite seu segundo Número: '))
aura = input('digite seu valor + | - | * | / : ')

soma = primeiro_numero + segundo_numero
subtracacao = primeiro_numero - segundo_numero
multipicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

match aura:
    case '+' :
        print(f'sua soma {soma}')
    case '-':
        print(f'sua divisão{subtracacao}')
    case '*' :
        print(f'sua multiplicaão {multipicacao}')
    case '/':
        print(f'sua divisão{divisao}')