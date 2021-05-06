v=[3,1,5,5,4,1,2,9]
def componentes(v):
    vi=[]
    vi.append(v[0])
    p=True
    for i in range(0,len(v)):
        for j in range(0,len(vi)):
            if v[i]==vi[j]:
                p=False
        if p==True:
            vi.append(v[i])
        p=True
    return vi
                
print componentes(v)
