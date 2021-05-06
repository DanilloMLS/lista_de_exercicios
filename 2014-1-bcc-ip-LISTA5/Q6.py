v=[3,1,5,5,4,1,2,9]
valor=6

def inserir_ord(v,valor):
    v.sort()
    u=[]
    b=True
    for i in range(0,len(v)):
        if (v[i]>=valor and b==True):
            u.append(valor)
            b=False
        u.append(v[i])
    if b==True:
        u.append(valor)
    return u
        
print inserir_ord(v,valor)
