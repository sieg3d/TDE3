#1. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-la por extenso.

'''
contagem = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove')

numero_escolhido = int(input('Escolha um numero entre 0 e 20:\n'))
if numero_escolhido <= 0 or numero_escolhido >= 20:
    print('Número inválido')
else:
    print(f'O número digitado foi o número {contagem[numero_escolhido-1]}.')
'''

#2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta quantos valores diferentes existem na lista.

'''
lista = []
for conteudo in range(10):
    valor = input(f'Insira o {conteudo+1}º valor: ')
    lista.append(valor)
    valores_diferentes = set(lista)


print(f'Os valores digitados foram: {lista} \nE quantidade de valores diferentes na lista são: {len(valores_diferentes)}')
'''

#3. Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista. No final mostre:
#a) Quantas vezes apareceu o valor 9.
#b) Em que posição foi digitado o primeiro valor 3.
#c) Quais foram os números pares.

'''
nova_lista = []
a = 0
c = []
for numero in range(4):
    num = int(input(f'Insira o {numero+1}º número: '))
    nova_lista.append(num)
    if num == 9:
        a+=1
    elif num%2 == 0:
        c.append(num)

print(f'O número 9 apareceu um total de {a}x.')
print(f'O número 3 foi digitado pela primeira vez na posição {nova_lista.index(3)}.')
print(f'Os números pares são: {c}')
'''

#4. Um dado é lançado 50 vezes, e o valor correspondente é armazenado em uma lista.
#Faça um programa que determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.

'''
import random

dado = []
numero_seis = 0
for lancamento in range(50):
    lado = random.randint(1,6)
    dado.append(lado)
    if lado == 6:
        numero_seis+=1
po = (numero_seis/50)*100

print(f'O face 6 foi sorteada um total de {numero_seis}x e o seu percentual de ocorrencia foi {po:.2f}%.')
print(f'\nPara conferência, a lista é a seguinte:\n{dado}')
'''

#5. Faça um programa que leia uma lista vet de 10 números inteiros. O programa deve gerar, a partir da lista lida, uma outra lista pos que contenha apenas os valores
#inteiros positivos de vet. A partir do vetor pos, deve ser gerado uma outra lista semdup que contenha apenas uma ocorrência de cada valor de pos.

vet = [-1,-4,-3,-2,-1,1,2,3,4,1]
pos = []


for valores in vet:
    if valores > 0:
        pos.append(valores)
semdup = set(pos)
    
print(f'Os valores inteiros posivitos são: {pos}')
print(f'E contendo apenas uma ocorrêmnia: {semdup}')
