nome = 'Michel de Oliveira'
altura = 1.78
peso = 60
imc = 60 / 1.78 ** 1.78  #  = peso / (altura x altura)

#F-String formatação de String
l_1 = f'{nome} tem {altura:.2f} de altura,'
l_2 = f'pesa {peso} quilos e seu IMC é de'
l_3 = f'{imc:.2f}'

print(l_1, l_2, l_3)

print(nome, 'tem', altura, 'de altura', 'pesa', peso, 'quilos e seu IMC é de', imc)

# Michel tem 1,78 de altura, pesa 60 quilos e seu IMC é

#metodo Format

a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} a={nome1} b={nome2} c={nome3:.2f}'

formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)


print('"Já sei!"')

divisao = 100 / 10

print(divisao)