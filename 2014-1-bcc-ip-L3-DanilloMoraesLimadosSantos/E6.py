data=raw_input("Digite sua data de nascimento: ")
jan="Janeiro"
fev="Fevereiro"
mar="Março"
abr="Abril"
mai="Maio"
jun="Junho"
jul="Julho"
ago="Agosto"
setm="Setembro"
out="Outubro"
nov="Novembro"
dez="Dezembro"

extenso=""

dia=data[:2]
mes=data[3:5]
ano=data[6:10]

if mes == "01": extenso=jan
elif mes == "02": extenso=fev
elif mes == "03": extenso=mar
elif mes == "04": extenso=abr
elif mes == "05": extenso=mai
elif mes == "06": extenso=jun
elif mes == "07": extenso=jul
elif mes == "08": extenso=ago
elif mes == "09": extenso=setm
elif mes == "10": extenso=out
elif mes == "11": extenso=nov
elif mes == "12": extenso=dez

print ("Você nasceu em"),dia,("de"),extenso,("de"),ano
