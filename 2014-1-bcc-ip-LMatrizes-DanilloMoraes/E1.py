# -*- coding: cp1252 -*-
def transposta(a):
    #Abre o arquivo especificado
    a=open(a)
    texto=a.readlines()
    #Fecha o arquivo
    a.close()
    #Matriz que receber� o conte�do do arquivo
    m=[]
    #Estruturas de repeti��o que criaram a matriz
    for i in range(len(texto)):
        m.append(texto[i].split(" "))
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j]=int(m[i][j])
    #Vari�vel que receber� a matriz m transposta
    t=[]
    #Estruturas que criar�o a matriz t
    for i in range(len(texto)):
        t.append(texto[i].split(" "))
    for i in range(len(t)):
        for j in range(len(t)):
            t[i][j]=int(m[j][i])
    return t
