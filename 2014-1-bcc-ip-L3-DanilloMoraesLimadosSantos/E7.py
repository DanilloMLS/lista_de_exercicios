# -*- coding: cp1252 -*-
fra=raw_input("Digite uma frase: ")
frase=fra.lower()
i=0
conta_espaco=0
conta_vogal=0
for i in range(0,len(frase)):
    if frase[i]==(" "):
        conta_espaco += 1
    if frase[i]=="a" or frase[i]=="e" or frase[i]=="i" or frase[i]=="o" or frase[i]=="u":
        conta_vogal += 1
    if frase[i]=="�" or frase[i]=="�" or frase[i]=="�" or frase[i]=="�" or frase[i]=="�" or frase[i]=="�" or frase[i]=="�":
        conta_vogal += 1

print ("Essa frase tem"),conta_espaco,("espa�os.")
print ("Essa frase tem"),conta_vogal,("vogais.")
