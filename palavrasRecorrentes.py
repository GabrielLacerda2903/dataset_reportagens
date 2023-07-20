lista=open("saidas/csvTratado.csv",'r').readlines()
lista.pop(0)

palavras=[]
qtd=[]
for i in lista:
    j=i.split(',')[0].split(" ")
    for o in j:
        if len(o)>=5:
            k=o.lower().replace("'","")
            if k not in palavras:
                palavras+=[k]
                qtd+=[0]
            qtd[palavras.index(k)]+=1


palavraOrdenada=[]
qtdOrdenada=[0]
k=0
for i in qtd:
    w=0
    for j in qtdOrdenada:
        if i>j:
            qtdOrdenada.insert(w,qtd[k])
            palavraOrdenada.insert(w,palavras[k])
            break
        w+=1
    k+=1
    
print(qtdOrdenada[:20])
print(palavraOrdenada[:20])