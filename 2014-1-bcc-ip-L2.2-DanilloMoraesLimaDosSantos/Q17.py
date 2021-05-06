mquad=input("Digite o tamanho da área a ser pintada: ")
qtinta=round((mquad/6.)*1.1,0)
latas=round((qtinta/18),0)
galoes=round((qtinta/3.6),0)
mistlata=round((qtinta/18),0)
mistgaloes=round(((qtinta % 18)/3.6),0)

precolata=latas*80
precogaloes=galoes*25
precomist=(mistlata*80)+(mistgaloes*25)

print ("Você vai precisar de"),qtinta,("L de tinta. Isso custará:")
print precolata,("reais comprando apenas latas de 18 L,"),latas,("latas")
print precogaloes,("reais comprando apenas galões de 3.6 L,"),galoes,("galões")
print precomist,("reais comprando galões e latas,"),mistlata,("latas e"),mistgaloes,("galoes")
