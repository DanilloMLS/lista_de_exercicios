tel=raw_input("Digite o n�mero do telefone: ")
numtel=""
tel8=""
telcorrigido=""
i=0

for i in range(0,len(tel)):
    
    if tel[i]!="-":
        numtel+=tel[i]

if len(numtel)<8:
    tel8="3"+numtel
else:
    tel8+=numtel

for i in range(0,len(tel8)):
    telcorrigido+=tel8[i]
    if i==3:
        telcorrigido+="-"

print ("Telefone possui"),len(numtel),("d�gitos.")
if len(numtel)<8:
    print("Vou acrescentar o d�gito tr�s na frente.")
print ("Telefone corrigido sem formata��o:"),tel8
print ("Telefone corrigido com formata��o:"),telcorrigido
