from random import choice
aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')
Lista = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteado = choice(Lista)
print('O(a) aluno(a) escolhido(a) foi {}.'.format(sorteado))

#Outra maneira:
'''import random
aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')
Lista = [aluno_1, aluno_2, aluno_3, aluno_4]
num = random.randint(1, 4)
print('O(a) aluno(a) escolhido(a) foi {}.'.format(Lista[num-1]))'''


#Outra maneira:
'''import random
um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
tres = input('Terceiro aluno: ')
quatro = input('Quarto aluno: ')
num = random.randint(1, 4)
if num == 1:
            print('O(a) aluno(a) escolhido(a) foi {}.'.format(um))
elif num == 2:
            print('O(a) aluno(a) escolhido(a) foi {}.'.format(dois))
elif num == 3:
            print('O(a) aluno(a) escolhido(a) foi {}.'.format(tres))
else:
            print('O(a) aluno(a) escolhido(a) foi {}.'.format(quatro))'''


