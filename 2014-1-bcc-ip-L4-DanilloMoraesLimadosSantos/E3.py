# -*- coding: cp1252 -*-
#Programa que faz uma somatória com base em um número num fornecido pelo usuário
import math
num = int(raw_input("Digite um número: "))
#Variável que guarda a somatória
s = 0
#Estrutura que faz a somatória e guarda ela na variável s
for i in range(0,num+1):
    s = s + (1./pow(2,i))
print "Somatória: ", s
