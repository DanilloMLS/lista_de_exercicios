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


