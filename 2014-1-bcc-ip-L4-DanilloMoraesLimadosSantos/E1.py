# -*- coding: cp1252 -*-
#Programa que recebe uma quantia qualquer de números digitados pelo usuário
#e encontra o menor, o maior e as média dos números digitados
#Variáveis usadas no programa
n = int(raw_input("Digite um novo número:"))
maior = n
menor = n
soma = 0
media = 0
cont = 0
#Estrutura de repetição para avaliar o número digitado
#O programa é encerrado se for digitado -1
while (n != -1):
    #Verifica se o número digitado é maior que o anterior
    if (n > maior):
        maior = n
    #Verifica se o número digitado é menor que o anterior
    if (n < menor):
        menor = n
    #Essas variáveis serão usadas para calcular a média dos números digitados
    soma += n
    cont += 1
    n = int(raw_input("Digite um novo número:"))

media = float(soma)/cont
print ("A média é: "), media
print ("O maior número é: "), maior
print ("O menor número é: "), menor
