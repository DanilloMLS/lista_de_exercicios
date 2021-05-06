# -*- coding: cp1252 -*-
#Programa que ordena um conjunto de 4 números
#determinados pelo usuário
#Lista que vai receber os números
lista=[None]*4
print ("Digite os números: ")
#Estrutura de repetição que vai receber os números do usuário
for i in range(0,4):
    lista[i]=int(raw_input("->"))

#Essa variável será usada para a troca dos números durante a ordenação da lista
troca=0
#Estrutura responsável pela ordenação da lista
for i in range(0,4):
    for j in range(0,4):
        if lista[i]<lista[j]:
            troca=lista[i]
            lista[i]=lista[j]
            lista[j]=troca

print lista
