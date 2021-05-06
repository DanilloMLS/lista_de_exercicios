peso=input("Digite o peso total dos peixes pescados: ")
excesso=peso-50
if excesso > 0:
    multa=excesso*4
    print("Excesso:"),excesso,("acima de 50 Kg; multa:"),multa,("reais")
else:
    multa=0
    excesso=0
    print("Excesso:"),excesso,("acima de 50 Kg; multa:"),multa,("reais")
