mquad=input("Digite o tamanho da �rea a ser pintada: ")
qtinta=round((mquad/6.)*1.1,0)
latas=round((qtinta/18),0)
galoes=round((qtinta/3.6),0)
mistlata=round((qtinta/18),0)
mistgaloes=round(((qtinta % 18)/3.6),0)

precolata=latas*80
precogaloes=galoes*25
precomist=(mistlata*80)+(mistgaloes*25)

print ("Voc� vai precisar de"),qtinta,("L de tinta. Isso custar�:")
print precolata,("reais comprando apenas latas de 18 L,"),latas,("latas")
print precogaloes,("reais comprando apenas gal�es de 3.6 L,"),galoes,("gal�es")
print precomist,("reais comprando gal�es e latas,"),mistlata,("latas e"),mistgaloes,("galoes")
