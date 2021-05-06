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
        

