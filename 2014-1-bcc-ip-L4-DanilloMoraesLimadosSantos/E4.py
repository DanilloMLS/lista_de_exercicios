# -*- coding: cp1252 -*-
#Programa que calcula se um numero dado pelo usuário é perfeito
numero = 0
#Variável que guarda a soma dos divisores desse número
soma = 0
#Estrutura que verifica se o número é menor que zero e inteiro
while (numero<=0):
    try:
        numero = int(raw_input("Digite um número: "))
        if numero<=0:
            print ("O número deve ser maior que zero.")
    except:
        print ("O número deve ser inteiro e maior que zero.")
#Estrutura que soma os divisores de numero
for i in range (1,numero-1):
    if (numero % i == 0):
        soma += i
#Condição que verifica se a soma dos divisores de numero e igual a ele mesmo
if (numero == soma):
    print ("Esse número é perfeito.")
else:
    print ("Esse número não é perfeito.")
