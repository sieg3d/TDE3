#1. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-la por extenso.


contagem = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove')

numero_escolhido = int(input('Escolha um numero entre 0 e 20:\n'))
if numero_escolhido <= 0 or numero_escolhido >= 20:
    print('Número inválido')
else:
    print(f'O numéro digitado foi o número {contagem[numero_escolhido-1]}.')


#2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta quantos valores diferentes existem na lista.

'''
lista = []
for conteudo in range(10):
    valor = input(f'Insira o {conteudo+1}º valor: ')
    lista.append(valor)
    valores_diferentes = set(lista)


print(f'Os valores digitados foram: {lista} \nE quantidade de valores diferentes na lista são: {len(valores_diferentes)}')
'''