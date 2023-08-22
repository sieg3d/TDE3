#1. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-la por extenso.

contagem = ('','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove')

numero_escolhido = int(input('Escolha um numero entre 0 e 20:\n'))
if numero_escolhido <= 0 or numero_escolhido >= 20:
    print('Número inválido')
else:
    print(f'O numéro digitado foi o número {contagem[numero_escolhido]}.')
