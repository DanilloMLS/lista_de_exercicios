nome=raw_input("Digite seu nome: ")
i=0
s=len(nome)+1
for i in range(0,len(nome)+1):
    s=s-1
    print nome[:s]
