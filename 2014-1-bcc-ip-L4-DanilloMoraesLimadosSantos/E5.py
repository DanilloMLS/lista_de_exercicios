# -*- coding: cp1252 -*-
#Programa que soma os quadrado dos n primeiros n�meros naturais com n dado pelo usu�rio
numero = int(raw_input("Digite um n�mero: "))
#Vari�vel que recebe a soma dos quadrados
soma = 0
#Estrutura de repeti��o que soma os quadrados dos n�meros
for i in range(1,numero+1):
    soma += i**2

print ("Soma dos quadrados: "),soma
