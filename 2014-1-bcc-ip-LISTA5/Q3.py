u=[2,2,2]
v=[1,1,1]
def produto(u,v):
    if len(u)!=len(v):
        return "Esses vetores tem tamanhos diferentes."
    prod=0
    for i in v:
        prod+=i*u[i]
    return prod

print produto(u,v)

