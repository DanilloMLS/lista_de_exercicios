mb=input("Digite o tamanho do arquivo em MB: ")
v=input("Digite a velocidade da conexão com a Internet em Mbps: ")

bits=1000000*v
kb=1024*8
valor=bits/kb

s=(mb*1024)/valor
t=round((s/60),2)

print ("O tempo de download em minutos é de:"),t,("minutos")
