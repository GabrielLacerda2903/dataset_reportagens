import os
from unidecode import unidecode as uni

lista=os.listdir("dataset") # Cria uma lista com os nomes de todos os arquivos do dataset #

x=0
for i in lista:
    lista[x]=open("dataset/"+i).readlines() # Lê cada arquivo #
    if lista[x]!=[]:    
        j = lista[x][0].split(":")
        if len(j)>2: # quando o título da matéria tem ":" #
            j.pop(0)
            j="".join(j)
        else:
            j=j[1]
        lista[x][0]=uni(j).replace(",","").strip()
        lista[x][1]=uni(lista[x][1].split(":")[1]).strip()
        lista[x][2]=lista[x][2].split(":")[1].strip()
        lista[x][3]=lista[x][3].split(":")[1].split('/')[0].strip()
    x+=1

lista=list(filter(None, lista))

tratada=open("saidas/csvTratado.csv","w")
tratada.write('titulo,autor,tema,mes\n')
for x in lista:
    tratada.write(f'{x[0]},{x[1]},{x[2]},{x[3]}\n')
tratada.close()