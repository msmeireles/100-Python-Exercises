#nome = str(input('Digite seu nome completo: ')).strip()
#print('Analisando seu nome...')
#print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
#print('Seu nome em minúsculas é: {}'.format(nome.lower()))
#lista = nome.split()
#junto = ''.join(lista)
#print('Seu nome tem ao todo {} letras.'.format(len(junto)))
#print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome.split()[0],len(nome.split()[0])))

#2
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome.split()[0],len(nome.split()[0])))






















