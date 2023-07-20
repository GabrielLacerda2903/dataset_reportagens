lista=open("saidas/csvTratado.csv",'r').readlines()
lista.pop(0)

autores=[]
qtd=[]
for i in lista:
    o=i.split(',')[1]
    if o not in autores:
        autores+=[o]
        qtd+=[0]
    qtd[autores.index(o)]+=1

primeiro=0
segundo=0
terceiro=0
for i in qtd:
    if i > primeiro:
        terceiro=int(segundo)
        segundo=int(primeiro)
        primeiro=i
    elif i>segundo:
        terceiro=int(segundo)
        segundo=i
    elif i>terceiro:
        terceiro=i

primeiro=autores[qtd.index(primeiro)]
segundo=autores[qtd.index(segundo)]
terceiro=autores[qtd.index(terceiro)]

arq=open('saidas/pubicacoesPorAutor.txt','w')
arq.write('AUTORES\n')
arq.write('='*48)
j=0
for i in autores:
    arq.write('\nNome: '+str(autores[j])+'\nPublicações: '+str(qtd[j])+'\n')
    j+=1

arq.write('='*48)
arq.close()