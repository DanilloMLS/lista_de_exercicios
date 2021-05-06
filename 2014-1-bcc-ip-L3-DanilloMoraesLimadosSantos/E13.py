import sys
import string
import random

arquivo=open('palavras.txt','r')

lista_palavras=arquivo.readlines()
palavra_certa=random.choice(lista_palavras)
palavra=list(palavra_certa)
palavra_emb=palavra
random.shuffle(palavra_emb)
tamanho=len(palavra)

i=0
tentativas=6
erros=0

while 1:
    erros=0
    print ("Faltam"),tentativas,("tentativas.")
    if tentativas==0:
        break
    for i in range(0,len(palavra_emb)):
        if palavra_emb != "\n" or palavra_emb!=" ":
            print palavra_emb[i],
    palpite=raw_input("\nDigite a palavra: ").lower()
    for i in range (0,len(palpite)):
        if palpite[i]!=palavra_certa[i]:
            erros+=1
    if erros > 0:
        tentativas-=1
    elif erros == 0:
        break
if erros == 0:
    print ("Parabéns! Você acertou a palavra!")
elif tentativas == 0:
    print ("Você errou a palavra! A palavra era:"),palavra_certa
