frase=raw_input("Digite uma frase: ")
fraselow=""
i=0
for i in range(0,len(frase)):
    if frase[i]!=" " and frase[i]!="." and frase[i]!="," and frase[i]!=";" and frase[i]!=":" and frase[i]!="?" and frase[i]!="!":
        fraselow=fraselow+frase[i]

f1palin=fraselow.lower()
f2palin=fraselow.lower()[::-1]

p=0
for i in range(0,len(fraselow)):
    if f1palin[i]==f2palin[i]:
        p+=1

if p==len(fraselow):
    print ("A sequência digitada: '"),frase,("' é um palindromo")
else:
    print ("A sequência digitada: '"),frase,("' não é um palindromo")
