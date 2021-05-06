# -*- coding: cp1252 -*-
def maior_dif(v):
    maior=0
    a=0
    b=0
    p1=0
    p2=0
    for i in range(0,len(v)):
        if i>0:
            if v[i]>v[i-1]:
                a=v[i]
                b=v[i-1]
            else:
                a=v[i-1]
                b=v[i]
            if maior<(a-b):
                maior=a-b
                if v[i]>v[i-1]:
                    p1=i
                    p2=i-1
                else:
                    p1=i-1
                    p2=i
    return "Maior diferenca:",maior,"posicoes:",p1,p2
