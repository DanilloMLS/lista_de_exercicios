cpf=raw_input("Digite seu CPF no formato 000.000.000-00: ")
ncpf=""

i=0
for i in range(0,len(cpf)):
    if cpf[i]!="." and cpf[i]!="-":
        ncpf+=cpf[i]

print ncpf
n0=int(ncpf[0])
n1=int(ncpf[1])
n2=int(ncpf[2])
n3=int(ncpf[3])
n4=int(ncpf[4])
n5=int(ncpf[5])
n6=int(ncpf[6])
n7=int(ncpf[7])
n8=int(ncpf[8])
n9=int(ncpf[9])
n10=int(ncpf[10])

v1=0
v2=0
p=0
s=0

v1=(n0*10)+(n1*9)+(n2*8)+(n3*7)+(n4*6)+(n5*5)+(n6*4)+(n7*3)+(n8*2)
x=v1%11
if x >= 2:
    p=11-x
else:
    p=0

v2=(n0*11)+(n1*10)+(n2*9)+(n3*8)+(n4*7)+(n5*6)+(n6*5)+(n7*4)+(n8*3)+(n9*2)
y=v2%11
if y >= 2:
    s=11-y
else:
    s=0

if p==n9 and s==n10:
    print ("O cpf informado é válido.")
else:
    print("O cpf informado não é válido.")
