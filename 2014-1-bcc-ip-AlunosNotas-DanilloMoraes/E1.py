# -*- coding: cp1252 -*-
def media(arquivo):
    #Abre, l� e fecha o arquivo
    a=open(arquivo)
    texto=a.readlines()
    a.close()

    #Vari�vel que conter� o conte�do da vari�vel texto em forma de matriz
    alunos_notas=[]
    for i in range(len(texto)):
        alunos_notas.append(texto[i].split(" "))

    #Vari�vel que conter� em forma de lista apenas o �ltimo valor de cada linha da matriz alunos_notas
    notas=[]
    for i in range(len(alunos_notas)):
        notas.append(alunos_notas[i][len(alunos_notas[i])-1])

    #Vari�vel que guarda em forma de matriz as notas, sendo que o ponto(.) servir�
    #para separar uma numero do outro. EX: 9.9 fica 9 9
    num=[]
    for i in range(len(notas)):
        num.append(notas[i].split("."))

    #Vari�veis para converter as notas para inteiro
    numerica=num
    n1=0
    n2=0
    for i in range(len(num)):
        n1=int(num[i][0])
        n2=int(num[i][1])
        numerica[i]=n1+(n2/10.)

    #M�dia das notas
    media=0
    soma=0
    for i in range(len(numerica)):
        soma+=numerica[i]
    media=soma/len(numerica)
    return media
