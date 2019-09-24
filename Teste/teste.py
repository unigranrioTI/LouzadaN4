bruto = float(input('Insira o salário bruto: '))
sexo = input('Insira o sexo do funcionário:[M/F] ')

if sexo == 'M':
  desc5 = (bruto*5)/100
  print('O seu salário é {}, seu desconto é de {} e seu salário líquido é: {}.'.format(bruto, desc5, bruto-desc5))

elif sexo == 'F':
  desc3 = (bruto*3)/100
  print('O seu salário é de {}, seu desconto é de {} e seu salário líquido é: {}.'.format(bruto, desc3, bruto-desc3))