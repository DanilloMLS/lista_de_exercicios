s1=raw_input("Digite o texto: ")
s2=raw_input("Digite outro texto: ")
i=0
ok=0
print s1,(","),len(s1),("caracteres")
print s2,(","),len(s2),("caracteres")
if len(s1)==len(s2):
    print ("As strings têm o mesmo tamanho.")
    for i in range (0,len(s1)):
        if s1[i]==s2[i]:
            ok+=1
    if ok==len(s1):
        print("As strings têm o mesmo conteúdo.")
else:
    print ("As strings têm são de tamanhos e conteúdos diferentes")
