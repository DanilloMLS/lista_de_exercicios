# -*- coding: cp1252 -*-
#Progrma que encontra os pares de números amigos até um número digitado pelo usuário
numero = int(raw_input("Digite um número: "))
#Variável que recebe a soma dos divisores de numero
s1 = 0
#Variável que recebe a soma dos divisores de s1
s2 = 0
print ("Lista dos pares de números amigos até"),numero,(":")
#Estrutura que verifica se o número i tem um número amigo
for i in range (1,numero):
    #Estrutura que encontra e soma os divisores de numero
    for j in range(1,i):
        if i % j == 0:
            s1 = s1 + j
    #Estrutura que encontra e soma os divisores de s1    
    for k in range(1,s1):
        if s1 % k == 0:
            s2 = s2 + k
    #Condição que define se i tem um número amigo
    if i == s2 and s1 < s2:
        print s1,s2
    s1 = 0
    s2 = 0
    
