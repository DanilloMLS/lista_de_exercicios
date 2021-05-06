# -*- coding: cp1252 -*-
#Programa que recebe votos como uma urna eletrônica
print ("Digite sua opção de voto:")
print ("83-Alan Turing")
print ("93-John von Neumann")
print ("00-Branco")
print ("Qualquer outro número será voto nulo.")
#Variável que recebe a opção de voto
voto = int(raw_input("Opção: "))
#Guarda os votos para o candidato Alan Turing
alan = 0
#Guarda os votos para o candidato Johnvon Neumann
john = 0
#Guarda os votos em branco
branco = 0
#Guarda os votos nulos
nulo = 0
#Estrutura de repetição que define qual variável vai receber o voto, enquanto voto for diferente de -1
while (voto != -1):
    if voto == 83:
        alan += 1
    elif voto == 93:
        john += 1
    elif voto == 00:
        branco += 1
    else:
        nulo += 1
    voto = int(raw_input("Opção: "))
#Essas variáveis calculam a quantia total de votos e a porcentagem para cada candidado e dos votos brancos e nulos
total = alan + john + branco + nulo
pt_alan = round((alan*100.0)/total,2)
pt_john = round((john*100.0)/total,2)
pt_branco = round((branco*100.0)/total,2)
pt_nulo = round((nulo*100.0)/total,2)
#Essas variáveis calculam a quantia de votos válidos e a porcentagem para cada candidato e dos votos em branco
valido = alan + john + branco
pv_alan = round((alan*100.0)/valido,2)
pv_john = round((john*100.0)/valido,2)
pv_branco = round((branco*100.0)/valido,2)
#Impressão do resultado da eleição
print("Candidato ++++++++ Votos +++ Percentagem +++ Percentagem dos votos válidos")
print("Alan Turing ++++++"),alan,("++++++++++"),pt_alan,("% +++++++++++"),pv_alan,("%")
print("John von Neumann +"),john,("++++++++++"),pt_john,("% +++++++++++"),pv_john,("%")
print("Brancos ++++++++++"),branco,("++++++++++"),pt_branco,("% +++++++++++"),pv_branco,("%")
print("Nulos ++++++++++++"),nulo,("++++++++++"),pt_nulo,("% ++++++++++++ X")
#Condição que verifica se haverá necessidade de uma nova eleição
if (pv_alan > 50):
    print ("Alan Turing foi eleito.")
elif (pv_john > 50):
    print ("John von Neumann foi eleito.")
else:
    print ("Uma nova eleição deve ser realizada.")
