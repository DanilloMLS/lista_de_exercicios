# -*- coding: cp1252 -*-
#Fun��o que retorna o k-en�simo d�gito de um n�mero inteiro n, com k e n  dados.
def k_enesimo(n,k):
    num=n/(10**(k-1))
    res=num%10
    return res
