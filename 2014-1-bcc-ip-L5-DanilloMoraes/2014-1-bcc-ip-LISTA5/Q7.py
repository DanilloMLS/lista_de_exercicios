def intersecao(v,u):
    w=[]
    for i in range(0,len(v)):
        for j in range(0,len(u)):
            if v[i]==u[j]:
                w.append(v[i])
    return w


