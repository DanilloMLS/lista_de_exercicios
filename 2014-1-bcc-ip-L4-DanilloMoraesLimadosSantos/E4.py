# -*- coding: cp1252 -*-
#Programa que calcula se um numero dado pelo usu�rio � perfeito
numero = 0
#Vari�vel que guarda a soma dos divisores desse n�mero
soma = 0
#Estrutura que verifica se o n�mero � menor que zero e inteiro
while (numero<=0):
    try:
        numero = int(raw_input("Digite um n�mero: "))
        if numero<=0:
            print ("O n�mero deve ser maior que zero.")
    except:
        print ("O n�mero deve ser inteiro e maior que zero.")
#Estrutura que soma os divisores de numero
for i in range (1,numero-1):
    if (numero % i == 0):
        soma += i
#Condi��o que verifica se a soma dos divisores de numero e igual a ele mesmo
if (numero == soma):
    print ("Esse n�mero � perfeito.")
else:
    print ("Esse n�mero n�o � perfeito.")
