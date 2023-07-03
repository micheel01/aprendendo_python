nome = 'Michel'
#print('M' in nome)
#print('l' in nome) #se ta no nome
#print('chel'  not in nome) # se nao ta no nome
#print('chel'   in nome) # se nao ta no nome

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que gostaria de encontrar: ')

if encontrar in nome:
    print (f'{encontrar} esta em {nome}')
else:
    print (f'{encontrar} nao esta em {nome}')

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)