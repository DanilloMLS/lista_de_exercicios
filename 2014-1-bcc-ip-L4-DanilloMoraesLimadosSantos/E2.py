# -*- coding: cp1252 -*-
#Programa que ordena um conjunto de 4 n�meros
#determinados pelo usu�rio
#Lista que vai receber os n�meros
lista=[None]*4
print ("Digite os n�meros: ")
#Estrutura de repeti��o que vai receber os n�meros do usu�rio
for i in range(0,4):
    lista[i]=int(raw_input("->"))

#Essa vari�vel ser� usada para a troca dos n�meros durante a ordena��o da lista
troca=0
#Estrutura respons�vel pela ordena��o da lista
for i in range(0,4):
    for j in range(0,4):
        if lista[i]<lista[j]:
            troca=lista[i]
            lista[i]=lista[j]
            lista[j]=troca

print lista
