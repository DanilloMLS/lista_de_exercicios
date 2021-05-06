# -*- coding: cp1252 -*-
#Programa que soma os quadrado dos n primeiros números naturais com n dado pelo usuário
numero = int(raw_input("Digite um número: "))
#Variável que recebe a soma dos quadrados
soma = 0
#Estrutura de repetição que soma os quadrados dos números
for i in range(1,numero+1):
    soma += i**2

print ("Soma dos quadrados: "),soma
