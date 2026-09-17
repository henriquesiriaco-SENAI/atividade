import os
os.system('cls')

renda_mensal = float(input('digite sua renda mensal'))
parcelas = int(input('valor das parcelas R$:  '))
emprestimo = int(input('deseja quantas emprestimo'))

if parcelas != renda_mensal *10 and  emprestimo >= (renda_mensal * 0,30):
    print('não pode ser aprovado pelo banco')
else:
    print('aprovado pelo banco')



