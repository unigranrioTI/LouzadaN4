peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
IMC = peso / altura**2
print('Seu peso é {}kg, sua altura é {}m, seu IMC é {:.2f}.'.format(peso, altura, IMC))