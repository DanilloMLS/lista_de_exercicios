# -*- coding: cp1252 -*-
def triangulo(a):
    #Abre o arquivo especificado
    a=open(a)
    texto=a.readlines()
    #Fecha o arquivo
    a.close()
    #Vari�vel que conter� a matriz
    m=[]
    #Estruturas que criar�o a matriz e a guardar�o em m
    for i in range(len(texto)):
        m.append(texto[i].split(" "))
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j]=int(m[i][j])
    #Vari�vel l�gica que ser� usada para definir se a matriz � ou n�o triangular
    tri=True
    #Estruturas que verificar�o se m � uma matriz triangular
    for i in range(len(m)-1):
        for j in range(1,len(m)):
            if m[i][j]!=0 and i!=j:
                tri=False
                break
    #Decis�o que retornar� o resultado da verifica��o
    if tri==True:
        return "� triangular"
    else:
        return "N�o � triangular"
