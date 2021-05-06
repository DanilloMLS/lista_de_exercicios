a=input("Digite sua altura: ")
s=raw_input("Digite o seu sexo:")
if s == "M":
    p=(72.7*a)-58
else:
    p=(62.1*a)-44.7
print ("Seu peso ideal é:"),p,("Kg")
