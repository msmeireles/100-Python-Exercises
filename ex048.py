cont = 0
soma = 0
for j in range(3, 500, 2):
    if j % 3 == 0 :
        cont += 1
        soma += j
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
