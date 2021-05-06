# -*- coding: cp1252 -*-
def triangulo(a):
    #Abre o arquivo especificado
    a=open(a)
    texto=a.readlines()
    #Fecha o arquivo
    a.close()
    #Variável que conterá a matriz
    m=[]
    #Estruturas que criarão a matriz e a guardarão em m
    for i in range(len(texto)):
        m.append(texto[i].split(" "))
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j]=int(m[i][j])
    #Variável lógica que será usada para definir se a matriz é ou não triangular
    tri=True
    #Estruturas que verificarão se m é uma matriz triangular
    for i in range(len(m)-1):
        for j in range(1,len(m)):
            if m[i][j]!=0 and i!=j:
                tri=False
                break
    #Decisão que retornará o resultado da verificação
    if tri==True:
        return "É triangular"
    else:
        return "Não é triangular"
