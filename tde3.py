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

'''
vet = [-1,-4,-3,-2,-1,1,2,3,4,1]
pos = []

for valores in vet:
    if valores > 0:
        pos.append(valores)

semdup = set(pos)
    
print(f'Os valores inteiros posivitos são: {pos}')
print(f'E contendo apenas uma ocorrêmnia: {semdup}')
'''

#6. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

'''
numeros = [19,73,82,46,5]
soma = sum(numeros)
produto = 1

for numero in numeros:
    produto *= numero


print(f'A soma dos numeros da lista é: {soma} e o produto de sua multiplicação é {produto}.')
print(f'Os números são:\n{numeros}')
'''

#7. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

'''
alturas = []
idades= []

for inf in range(5):
    idade = int(input(f'Insira a idade da {inf+1}ª pessoa: '))
    altura = float(input(f'Agora insira a altura da {inf+1}ª pessoa: '))
    idades.append(idade)
    alturas.append(altura)

alturas.reverse()
idades.reverse()

print(f'As alturas inseridas foram: {alturas}')
print(f'E as suas respectivas idades são: {idades}')
'''

#8. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a) "Telefonou para a vítima?"
#b) "Esteve no local do crime?"
#c) "Mora perto da vítima?"
#d) "Devia para a vítima?"
#e) "Já trabalhou com a vítima?"

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
#classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

'''
pessoa = []

a = input('Telefonou para a vítima? S/N ')
if a == 's':
    pessoa.append(1)
b = input('Esteve no local do crime? S/N ')
if b == 's':
    pessoa.append(1)
c = input('Mora perto da vítima? S/N ')
if c == 's':
     pessoa.append(1)
d = input('Devia para a vítima? S/N ')
if d == 's':
    pessoa.append(1)
e = input('Já trabalhou com a vítima? S/N ')
if e == 's':
    pessoa.append(1)

if sum(pessoa) == 5:
    print('Ah-há! Você é o Assassino!')
elif sum(pessoa) <= 4 and sum(pessoa) >= 3:
    print('Ora ora... temos um cumplice')
elif sum(pessoa) == 2:
    print('Não sei Rick. Parece suspeito!')
else:
    print('Sabe de nada! Inocente!')
'''

#9. Faça um programa que simule um lançamento de dados. Lance o dado 10 vezes e armazene os resultados em um vetor.
#Depois, monte um outro vetor contendo quantas vezes cada valor foi obtido. Imprima os dois vetores.
# Use uma função para gerar números aleatórios, simulando os lançamentos dos dados.
#Exemplo de uma possível saída:
#[3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
#[1, 0, 3, 1, 4, 1]

'''
import random

dado = []
lancamentos = [0]*6

for lance in range(10):
    numero = random.randint(1,6)
    dado.append(numero)
    if numero == 1:
        lancamentos[0] += 1
    elif numero == 2:
        lancamentos[1] += 1
    elif numero == 3:
        lancamentos[2] += 1
    elif numero == 4:
        lancamentos[3] += 1
    elif numero == 5:
        lancamentos[4] += 1
    elif numero == 6:
        lancamentos[5] += 1

print(f'Os números sorteados foram: {dado}')
print(f'Segue sequencia de quantidade de sorteios para cada numero: {lancamentos}')
'''

#10. Faça um programa que percorre um vetor e imprime na tela o valor mais próximo da média dos valores do vetor.
#Exemplo:
#vetor = [2.5, 7.5, 10.0, 4.0]
#média = 6.0
#Valor mais próximo da média = 7.5


qtd = int(input('Digite a quantidade de posições que terá a sua lista: '))
vetor = []
total = 0
media = 0
menor_distancia = 0

print(qtd)

for valor in range(qtd):
    numero = float(input(f'Digite o número {valor+1}'))
    vetor.append(numero)
    total += numero

media = total / qtd
print(total)
print(media)

for valor in range(qtd):
    distancia = abs(vetor[valor] - media)
    if menor_distancia ==0 or distancia < menor_distancia:
         menor_distancia = distancia

print(f'{total:.2f}')
print(media)
print(menor_distancia)
