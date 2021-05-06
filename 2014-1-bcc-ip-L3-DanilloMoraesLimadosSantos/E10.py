n=raw_input("Digite um número até 99: ")
num=int(n)
num1=int(n[0])
num2=int(n[1])

u=["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
e=["onze","doze","treze","quatorze","quinze","desesseis","desessete","dezoito","dezenove",]
d=["dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]

if num < 10:
    print u[num1]
elif num > 10 and num < 20:
    print e[i-11]
elif num == 10 or num == 20 or num == 30 or num == 40 or num == 50 or num == 60 or num == 70 or num == 80 or num == 90:
    print d[num1-1]
elif num > 20 and num < 30:
    print d[1],("e"),u[num2]
elif num > 30 and num < 40:
    print d[2],("e"),u[num2]
elif num > 40 and num < 50:
    print d[3],("e"),u[num2]
elif num > 50 and num < 60:
    print d[4],("e"),u[num2]
elif num > 60 and num < 70:
    print d[5],("e"),u[num2]
elif num > 70 and num < 80:
    print d[6],("e"),u[num2]
elif num > 80 and num < 90:
    print d[7],("e"),u[num2]
elif num > 90 and num < 100:
    print d[8],("e"),u[num2]
else:
    print ("número não válido.")
