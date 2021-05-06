v=[5,8,9,7]
u=[2,4,8,7]

def intersecao(v,u):
    w=[]
    for i in range(0,len(v)):
        for j in range(0,len(u)):
            if v[i]==u[j]:
                w.append(v[i])
    return w

print intersecao(v,u)
