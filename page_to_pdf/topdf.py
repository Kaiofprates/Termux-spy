import requests, os
import subprocess as sp
from tqdm import tqdm
#colors
neg = '\033[1m';cl= '\033[0;0m';red= '\033[31m';green = '\033[32m'
blue = '\033[34m';cian = '\033[36m';mag = '\033[35m'
#funcion
def list(nome):
    lista = open(nome+".txt","r")
    lista = lista.readlines()
    a = range(len(lista))

    for i in tqdm(a):
        url = requests.get("https://url-to-pdf-api.herokuapp.com/api/render?url="+lista[i].replace("\n",""))
        if(not url):
            print(red+neg+"Link invalido"+cl)
            pass
        else:
            pdf = open(nome+str(i)+'.pdf','wb')
            pdf.write(url.content)
            pdf.close()
            print(green+"\n\tSalvo como:"+red+nome+str(i)+'.pdf'+cl)

def pdf(nome):
    link = input("Link >>> ")
    a = range(1)
    print(mag+"BUSCANDO..."+cl)
    url = requests.get("https://url-to-pdf-api.herokuapp.com/api/render?url="+link)
    if(not url):
        print(red+neg+"Link invalido"+cl)
        pass
    else:
        for i in tqdm(a):
            pdf = open(nome+".pdf","wb")
            pdf.write(url.content)
            pdf.close()
        print(green+"Salvo como: "+cian+nome+".pdf"+cl)
#headers
print(blue+'                                    \n                                    \n`7MM"""Mq.                          \n  MM   `MM.                         \n  MM   ,M9 ,6"Yb.  .P"Ybmmm .gP"Ya  \n  MMmmdM9 8)   MM :MI  I8  ,M\'   Yb \n  MM       ,pm9MM  WmmmP"  8M"""""" \n  MM      8M   MM 8M       YM.    , \n.JMML.    `Moo9^Yo.YMMMMMb  `Mbmmd\' \n  mm              6\'     dP         \n  MM              Ybmmmd\'           \nmmMMmm ,pW"Wq.                      \n  MM  6W\'   `Wb                     \n  MM  8M     M8                     \n  MM  YA.   ,A9                     \n  `Mbmo`Ybmd9\'   ,,      ,...       \n`7MM"""Mq.     `7MM    .d\' ""       \n  MM   `MM.      MM    dM`          \n  MM   ,M9  ,M""bMM   mMMmm         \n  MMmmdM9 ,AP    MM    MM           \n  MM      8MI    MM    MM           \n  MM      `Mb    MM    MM           \n.JMML.     `Wbmd"MML..JMML.         \n                                    \n                                    ')
print(cian+'{:_^47}'.format('dev_kailp*jun18'))
print(neg+red+" * "+cl+neg+"Copie para a area de transferência a página que deseja converter."+cl)
w = input(neg+green+"\n\t1"+mag+" --- "+blue+" para apenas um site\n\t"+green+"2"+mag+" --- "+blue+" para lista de sites em formato txt\n\tseguindo a ordem de cada link em uma linha."+cian+"\n\t>>> ")
x = input(cian+"Digite o nome do arquivo: "+cl)
if(w == '1' or w == '01'):
    pdf(x)
if(w == '2' or w == '02'):
    list(x)
else:
    print(red+"\n\tESCOLHA INVÁLIDA"+cl)
