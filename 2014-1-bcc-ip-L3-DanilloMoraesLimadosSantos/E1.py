s1=raw_input("Digite o texto: ")
s2=raw_input("Digite outro texto: ")
i=0
ok=0
print s1,(","),len(s1),("caracteres")
print s2,(","),len(s2),("caracteres")
if len(s1)==len(s2):
    print ("As strings t�m o mesmo tamanho.")
    for i in range (0,len(s1)):
        if s1[i]==s2[i]:
            ok+=1
    if ok==len(s1):
        print("As strings t�m o mesmo conte�do.")
else:
    print ("As strings t�m s�o de tamanhos e conte�dos diferentes")
