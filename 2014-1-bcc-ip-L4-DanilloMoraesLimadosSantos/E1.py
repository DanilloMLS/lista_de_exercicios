# -*- coding: cp1252 -*-
#Programa que recebe uma quantia qualquer de n�meros digitados pelo usu�rio
#e encontra o menor, o maior e as m�dia dos n�meros digitados
#Vari�veis usadas no programa
n = int(raw_input("Digite um novo n�mero:"))
maior = n
menor = n
soma = 0
media = 0
cont = 0
#Estrutura de repeti��o para avaliar o n�mero digitado
#O programa � encerrado se for digitado -1
while (n != -1):
    #Verifica se o n�mero digitado � maior que o anterior
    if (n > maior):
        maior = n
    #Verifica se o n�mero digitado � menor que o anterior
    if (n < menor):
        menor = n
    #Essas vari�veis ser�o usadas para calcular a m�dia dos n�meros digitados
    soma += n
    cont += 1
    n = int(raw_input("Digite um novo n�mero:"))

media = float(soma)/cont
print ("A m�dia �: "), media
print ("O maior n�mero �: "), maior
print ("O menor n�mero �: "), menor
