frase = raw_input("Digite uma frase: ")
traduz = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','v','x','y','z'],
         ['4','8','[','|)','3','|=','6','#','1','_/','|<','|_','//.','//','0','|^','9','|2','5','7','(_)','V','vv','><','`/','2']]
frase_traduzida=""

for i in frase.lower():
    if i in traduz[0]:
        frase_traduzida += traduz[1][traduz[0].index(i)]
    else:
        frase_traduzida += i

print frase_traduzida
