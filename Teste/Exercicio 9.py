cod = int(input('Digite o código do item [100/101/102/103]: '))
quant = int(input('Digite a quantidade: '))

if cod == 100:
    valorcacho = 5.2
    print('Você comprou {} cachorros quente(s) com o valor total de: {}.'.format(quant, valorcacho*quant))

elif cod == 101:
    valorham = 5.2
    print('Você comprou {} hamburguers com o valor total de: {}.'.format(quant,valorham*quant))

elif cod == 102:
    valorcheese = 7.3
    print('Você comprou {} cheeseburguer com o valor total de: {}.'.format(quant,valorcheese*quant))

elif cod == 103:
    refri = 5.0
    print('Você comprou {} refrigerantes com o valor total de: {}.'.format(quant,refri*quant))

else:
    print('Digite um código válido.')