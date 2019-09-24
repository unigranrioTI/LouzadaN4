nota1 = float(input('Insira o valor da primeira nota: '))
nota2 = float(input('Insira o valor da segunda nota: '))
media = (nota1+nota2)/2
if media >= 7:
  print('Aprovado.')

elif media < 7:
  nota3 = float(input('Você não foi aprovado, digite o valor da terceira nota: '))


  novaMedia = ((nota3*2)+ nota1 + nota2) /3
  print('O aluno foi aprovado 'if media >= 6 else' reprovado.')
