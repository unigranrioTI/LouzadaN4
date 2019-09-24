import math
x1 = int(input('Insira a coordenada de x1: '))
x2 = int(input('Insira a coordenada de x2: '))
y1 = int(input('Insira a coordenada de y1: '))
y2 = int(input('Insira a coordenada de y2: '))
D = math.sqrt(x2-x1)**2 + (y2-y1)**2
print('A sua distância é de {}'.format(D))