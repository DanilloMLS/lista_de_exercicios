def produto(u,v):
    if len(u)!=len(v):
        return "Esses vetores tem tamanhos diferentes."
    prod=0
    for i in v:
        prod+=i*u[i]
    return prod

