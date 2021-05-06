def palindromo(v):
    c=v[::-1]
    p=True
    for i in range(1,len(v)):
        if c!=v:
              p=False  
    return p
