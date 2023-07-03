# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
#entrada = input('[E]ntrar [S]air: ')
#senha_digitada = input('Senha: ')

#senha_permitida = '123456'

#if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
 #    print('Entrar')
#else:
#    print('Sair')

# Avaliação de curto circuito
#print(True and False and True)
#senha = 0 or False or 0 or 'abc' or True
#print(senha)

#senha_1 = input('Senha: ') or 'Sem senha'
#print(senha_1)

#if 0 and 1:
 #   print(True and 1)

#NOT inverte expressoes

#senha = input('Senha: ')
#if senha != '123456':
#    print('Entrou')
#else:
#    print('Senha incorreta')

#if not senha:
 #   print('Voce n digitou nada')
print(not True) #false
print(not False) #True
