# -*- coding: cp1252 -*-
class polinomio:
    def __init__(self,lista,x):
        self.lista=l
        self.x=x
    #Classe que vai imprimir o polin�mio
    def printar(self):
        c=len(self.lista)-1
        for i in self.lista:
            if c!=0:
                if i!=0:
                    print i,"x^",c,"+",
            else:
                print i
            c=c-1
    #Classe que vai imprimir o resultado do polin�mio com base em um x dado
    def poli(self):
        self.lista
        c=len(self.lista)-1
        r=0
        for i in self.lista:
            r+=i*(self.x**c)
            c=c-1
        print r
    #Classe que retorna o grau do polin�mio
    def grau(self):
        c=len(self.lista)-1
        print c
    #Classe que calcula a derivada do polin�mio
    def derivada(self):
        t=[]
        t=self.lista
        c=len(self.lista)-1
        for i in range(len(t)):
            t[i]=self.lista[i]*c
            c=c-1
        c=len(t)-1
        u=True
        for i in t:
            if c>1:
                if i!=0:
                    print i,"x^",c-1,"+",
            elif u==True:
                print i
                u=False
            c=c-1
