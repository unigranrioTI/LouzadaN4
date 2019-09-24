amostra = int(input('Insira o valor da amostra: '))
carb = int(input('Insira a quantidade de carbono: '))
rok = int(input('Insira a dureze: '))
resis = int(input('Insira a resistênica psi: '))

if carb < 7 and rok > 50 and resis > 80000:
    print('A amostra {} obteve o grau 10.'.format(amostra))
elif carb < 7 and rok > 50 or resis > 80000:
    print('A amostra {} obteve o grau 9.'.format(amostra))
elif carb < 7 or rok > 50 or resis > 80000:
    print('A amostra {} obteve o grau 8.'.format(amostra))
else:
    print('A amotra {} obteve o grau 7.'.format(amostra))
