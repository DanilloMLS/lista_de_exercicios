# -*- coding: cp1252 -*-
#Programa que faz uma somat�ria com base em um n�mero num fornecido pelo usu�rio
import math
num = int(raw_input("Digite um n�mero: "))
#Vari�vel que guarda a somat�ria
s = 0
#Estrutura que faz a somat�ria e guarda ela na vari�vel s
for i in range(0,num+1):
    s = s + (1./pow(2,i))
print "Somat�ria: ", s
