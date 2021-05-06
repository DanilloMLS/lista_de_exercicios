r=[1,2,5,3,1,2,3,4,4,1,2,5,1,2,5,4,5,2,1,3,5,4,5,1,2,3,5,2,5,4,4,2,4,4,2,3,2,1,2,3,5,4,2,3,1,5,3,2,4,4]
g=[1,2,3,3,1,2,3,4,4,1,2,5,1,2,5,4,5,2,1,3,5,4,5,1,2,3,5,2,5,4,4,2,4,4,2,3,2,1,2,3,5,4,2,3,1,5,3,2,4,4]
def correcao(g,r):
    acertos=0
    while(len(r)<len(g)):
        if len(r)<gen(g):
            r.append(0)
    for i in range(0,len(r)):
        if r[i]==g[i]:
            acertos+=1
    return acertos
print correcao(g,r)
