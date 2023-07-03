entrada_1 = input('Digite um numero ') 
if entrada_1.isdigit():
   int_numero_1 = int(entrada_1)
else:
    print('Voce nao digitou um numeo inteiro')
par_impar = int_numero_1 % 2 == 0

if par_impar == True:
    print('O numero é par')
else:
    par_impar == False
    print('O numero é impar')

entrada_2 = input('Qual a hora que voce esta vendo esse programa?: ')
try:

    hora = int(entrada_2)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17: 
        print('Boa Tarde')
    elif hora >= 18 and hora <= 23 :
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
   print('Digite apenas numeros inteiros')
    
nome_usuario = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome_usuario)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é Normal')
    else:
     print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')



