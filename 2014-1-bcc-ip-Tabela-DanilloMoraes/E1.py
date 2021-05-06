# -*- coding: cp1252 -*-
#Abre o arquivo Tabela.dat
a=open("Tabela.dat")
texto=a.readlines()
#Fecha o arquivo
a.close()
#Apaga a primeira e a última linha do arquivo, restando apenas os números
del texto[0]
del texto[9]
m=[]
#Estrutura que divide o arquivo em blocos separados usando o espaço como parâmetro
for i in range(len(texto)):
    m.append(texto[i].split(" "))
#Estrutura que deleta a primeira coluna do que será a matriz
for i in range(len(m)):
    del m[i][0]
#Estruturas que criam a matriz
for i in range(len(m)):
    for j in range(len(m)):
        m[i][j]=int(m[i][j])
#Função que calcula o custo
def custo(lista):
    #Variável que guardará o custo
    c=0
    #Estrutura calcula o custo
    for i in range(len(lista)-1):
        c+=m[l[i]][l[i+1]]
    c+=m[l[-1]][l[0]]
    return c

#Pede a lista de cidades
l=[]
c=0
v=-1
t=True
print ("A lista deve passar por cada cidade ao menos uma vez")
#Estrutura que define se o valor digitado será ou não guardado no vetor e se o vetor tem ao menos 9 cidades
while(t==True):
    c=input("Digite: ")
    if c>=0 and c<=8 and c!=v:
        l.append(c)
        v=c
    if (c<0 or c>8) and len(l)>7:
        t=False
print custo(l)
