def correcao(g,r):
    acertos=0
    while(len(r)<len(g)):
        if len(r)<gen(g):
            r.append(0)
    for i in range(0,len(r)):
        if r[i]==g[i]:
            acertos+=1
    return acertos

