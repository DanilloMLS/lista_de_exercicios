salhora=input("Digite o quanto voc� ganha por hora: ")
hora=input("Digite quantas horas voc� trabalha por m�s: ")
salbruto=salhora*hora
ir=salbruto*0.11
inss=salbruto*0.08
sindicato=salbruto*0.05
descontos=ir+inss+sindicato
salliquido=salbruto-descontos
print("+ Sal�rio Bruto: R$"),salbruto
print("- IR: R$"),ir
print("- INSS: R$"),inss
print("- Sindicato: R$"),sindicato
print("= Sal�rio L�quido: R$"),salliquido
