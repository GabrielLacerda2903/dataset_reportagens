lista=open("saidas/csvTratado.csv",'r').readlines()
lista.pop(0)

meses=[0]*12
nomeMeses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
for i in lista:
    o=i.split(',')
    meses[int(o[3].strip())-1]+=1

primeiro=0
segundo=0
terceiro=0
for i in meses:
    if i > primeiro:
        terceiro=int(segundo)
        segundo=int(primeiro)
        primeiro=i
    elif i>segundo:
        terceiro=int(segundo)
        segundo=i
    elif i>terceiro:
        terceiro=i

primeiro=nomeMeses[meses.index(primeiro)]
segundo=nomeMeses[meses.index(segundo)]
terceiro=nomeMeses[meses.index(terceiro)]

print(primeiro,segundo,terceiro)