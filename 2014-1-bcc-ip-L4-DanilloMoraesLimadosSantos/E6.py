# -*- coding: cp1252 -*-
#Programa que mostra todos os subconjuntos de tr�s elementos, com n dado
n = int(raw_input("Digite um n�mero: "))
#Estrutura que ordenar� os n�meros, de 1 at� n
#A vari�vel i define a primeira coluna, j define a segunda e k a terceira
for i in range (1,n+1):
    for j in range (1,n+1):
        for k in range (1,n+1):
            if i < j and j < k:
                print i,j,k
        
            
