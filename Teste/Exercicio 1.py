tempoViagem = int(input('Digite o tempo gasto na viagem: '))
velMedia = int(input('Digite a velocidade média percorrida na viagem: '))
dist = (tempoViagem * velMedia)
litrosUsados = dist/12
print('A sua velocidade média foi de {} km/h, o tempo gasto na viagem foi de {} horas, a distância percorrida foi de {} km e quantidade de litros usados na viagem foi de {:.2f} litros.'.format(velMedia, tempoViagem, dist, litrosUsados))