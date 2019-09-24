sexMas = int(input('Digite quantos alunos do sexo masculinos possuem: '))
sexFem = int(input('Digite a quantidade de alunos do sexo feminino: '))
alunosApro = int(input('Digite a quantida de alunos aprovados: '))
totalAlunos = sexMas + sexFem
porcMas = sexMas*100 / totalAlunos
porcFem = sexFem*100 / totalAlunos
porcAprov = (alunosApro*100) / totalAlunos
print('O total de alunos é de: {}'.format(totalAlunos))
print('A porcentagem de alunos masculinos é {}%, e de feminino é de {}%, e a porcentagem de alunos aprovados é de {}%.'.format(porcMas, porcFem,porcAprov))