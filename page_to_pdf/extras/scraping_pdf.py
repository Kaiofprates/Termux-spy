import requests
from bs4 import BeautifulSoup

neg = '\033[1m';cl= '\033[0;0m';red= '\033[31m';green = '\033[32m'
blue = '\033[34m';cian = '\033[36m';mag = '\033[35m'

def salva(page):
    url = requests.get(page)
    soup = BeautifulSoup(url.content,'html.parser')
    doc = open('lista.txt','w')
    all_links = soup.find_all('a')
    for link in all_links:
        doc.write(link.get('href'))
        doc.write('\n')
        print(link.get('href'))
    doc.close()

def baixa(k):
    pdf = open(k+'.txt','r')
    pdf = pdf.readlines()
    flag = 1
    nome = 'IT'
    for link in pdf[:]:
        page = link.replace('\n','')
        doc = open(nome+str(flag)+'.pdf','wb')
        url = requests.get(page)
        doc.write(url.content)
        doc.close()
        flag = flag + 1
print(neg+green+" _    _        _                                 \n| |  | |      | |                                \n| |  | |  ___ | |__                              \n| |/\\| | / _ \\| '_ \\                             \n\\  /\\  /|  __/| |_) |                            \n \\/__\\/  \\___||_.__/             _               \n/  ___|                         (_)              \n\\ `--.   ___  _ __  __ _  _ __   _  _ __    __ _ \n `--. \\ / __|| '__|/ _` || '_ \\ | || '_ \\  / _` |\n/\\__/ /| (__ | |  | (_| || |_) || || | | || (_| |\n\\____/  \\___||_|   \\__,_|| .__/ |_||_| |_| \\__, |\n                         | |                __/ |\n                         |_|               |___/ ")

print(cian+'{:_^47}'.format('dev_kailp*jun18'))
op = input(red+'01'+mag+' ---'+blue+" para gerar uma lista de links.\n"+red+'02'+mag+' ---'+blue+' para usar uma lista pronta\n\t>>> '+cl)
if (op == '01' or op == '1'):
    li = input('\nLink: ')
    salva(li)
    print(red+neg+"\n\tIMPORTANTE ! As listas automáticas geralmente vêm com algums bugs\n\tassim, antes de baixar os links, observe o seguinte:\n\t"+red+"*"+cian+" não deve haver espaços entre os links, nem na primeira linha\n\t"+red+"*"+cian+" alguns links às vezes vem com mais de duas barras // "+green+"\n\tREINICIE O PROGRAMA E ESCOLHA A OPÇÃO 2"+cl)
if(op == '02' or op == '2'):
    q = input('Nome da lista: ')
    baixa(q)
else:
    print(red+"OPÇÃO INVÁLIDA"+cl)
