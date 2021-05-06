# -*- coding: cp1252 -*-
#Função que retorna o k-enésimo dígito de um número inteiro n, com k e n  dados.
def k_enesimo(n,k):
    num=n/(10**(k-1))
    res=num%10
    return res
