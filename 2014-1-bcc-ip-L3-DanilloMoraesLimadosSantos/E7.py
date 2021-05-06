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
    if frase[i]=="á" or frase[i]=="à" or frase[i]=="ã" or frase[i]=="é" or frase[i]=="ó" or frase[i]=="õ" or frase[i]=="ú":
        conta_vogal += 1

print ("Essa frase tem"),conta_espaco,("espaços.")
print ("Essa frase tem"),conta_vogal,("vogais.")
