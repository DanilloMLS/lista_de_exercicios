salhora=input("Digite o quanto você ganha por hora: ")
hora=input("Digite quantas horas você trabalha por mês: ")
salbruto=salhora*hora
ir=salbruto*0.11
inss=salbruto*0.08
sindicato=salbruto*0.05
descontos=ir+inss+sindicato
salliquido=salbruto-descontos
print("+ Salário Bruto: R$"),salbruto
print("- IR: R$"),ir
print("- INSS: R$"),inss
print("- Sindicato: R$"),sindicato
print("= Salário Líquido: R$"),salliquido
