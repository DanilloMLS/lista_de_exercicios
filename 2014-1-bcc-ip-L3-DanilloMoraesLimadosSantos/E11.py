import sys
import string
import random

abrir=open('palavras.txt','r')
base_dados=abrir.readlines()
p_inteira=random.choice(base_dados)
p_lista=[]
p_tracos=[]
tentativas=6
a_antes=0
a_agora=0

for char in range(len(p_inteira)):
    if p_inteira[char]!="\n":
        p_lista.append(p_inteira[char])
for char in range(len(p_inteira)):
    if p_inteira[char]!="\n":
        p_tracos.append("_ ")
print ("\nA palavra tem"),len(p_lista),("letras.")

while 1:
    if tentativas==0:
        break
    elif p_lista==p_tracos:
        break
    a_antes=a_agora
    print ("\nFaltam"),len(p_lista)-int(a_agora),("letras.")
    print ("Faltam"),tentativas,("tentativas.")
    mostrar_palavra=""
    for char in range(len(p_tracos)):
        mostrar_palavra=mostrar_palavra+p_tracos[char]
    print mostrar_palavra
    letra=raw_input("Digite uma letra: ").lower()
    for char in range(len(p_tracos)):
        if p_lista[char]==letra:
            p_tracos[char]=str(letra)
            a_agora+=1
    if a_antes==a_agora:
        tentativas -=1
if tentativas!=0:
    print("Parabéns! Você acertou a palavra!")
    print p_inteira
else:
    print("Você perdeu! A palavra era:"),p_inteira
