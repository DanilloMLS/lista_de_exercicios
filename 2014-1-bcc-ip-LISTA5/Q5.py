v=[3,1,5,5,4,1,2,9]
valor=3
p=0

def inserir(v,valor,p):
    u=[]
    pos=p-1
    if pos<0:
        pos=0
    for i in range(0,len(v)):
        if i==pos:
            u.append(valor)
        u.append(v[i])       
    return u

print inserir(v,valor,p)
