import requests
import re, os , time
import subprocess as sp

neg = '\033[1m';cl= '\033[0;0m';red= '\033[31m';green = '\033[32m'
blue = '\033[34m';cian = '\033[36m';mag = '\033[35m'

global bus,url,link

print(cian+' _______                                 \n(_______)                      _         \n _  _  _  _____   ____  ___  _| |_  ___  \n| ||_|| |(____ | / ___)/ _ \\(_   _)/ _ \\ \n| |   | |/ ___ || |   | |_| | | |_| |_| |\n|_|   |_|\\_____||_|    \\___/   \\__)\\___/ \n                                         \n'+cl)

#print(red+' ___      ___       __        _______     ______  ___________  ______    \n|"  \\    /"  |     /""\\      /"      \\   /    " \\("     _   ")/    " \\   \n \\   \\  //   |    /    \\    |:        | // ____  \\)__/  \\\\__/// ____  \\  \n /\\\\  \\/.    |   /\' /\\  \\   |_____/   )/  /    ) :)  \\\\_ /  /  /    ) :) \n|: \\.        |  //  __\'  \\   //      /(: (____/ //   |.  | (: (____/ //  \n|.  \\    /:  | /   /  \\\\  \\ |:  __   \\ \\        /    \\:  |  \\        /   \n|___|\\__/|___|(___/    \\___)|__|  \\___) \\"_____/      \\__|   \\"_____/    \n                                                                         \n'+cl)
print(cian+'{:_^47}'.format('dev_kailp*may18'))
print(cl)
print(neg+"*Copie o link da página com as respostas no site Dontpad e clique enter,\n!!!!NÃO  é necessário colar!!!!.\nO formato das respostas deverá seguir o modelo:\n\t[gabarito: a b c d e ]\n"+cl)
status, link = sp.getstatusoutput("termux-clipboard-get")
url = requests.get(link)

def enviar():
    quest = "gabarito: "+input("\n\tgabarito: ")
    post = requests.post(link, data = {'text':quest})
    print(green+"...postado com sucesso..."+cl)

def vibrate(x):
    for i in range(x):
        os.system("termux-vibrate -d 100 -f")

def pes(x):
    bus = re.findall(r'id="text">gabarito:(.*)</textarea>\n\t\t</div>\n\t\t\n\t\t<input',x)
    return bus
def chec(x):
    while not x:
        url = requests.get(link)
        print(red+"Escutando..."+cl)
        os.system("clear")
        x = re.findall(r'id="text">gabarito:(.*)</textarea>\n\t\t</div>\n\t\t\n\t\t<input',url.text)
    else:
        print(green+"Lendo"+cl)
        time.sleep(2)
        os.system("termux-vibrate -d 300 -f")
        time.sleep(2)
        x = str(x[0])
        x = x.split()
        for i in x[:]:
            time.sleep(2)
            if i == 'a':
                vibrate(1)
            if i == 'b':
                vibrate(2)
            if i == 'c':
                vibrate(3)
            if i == 'd':
                vibrate(4)
            if i == 'e':
                vibrate(5)
option = input(cian+"\n\tEscolha a opção: \n\t01.para postar gabarito\n\t02.para ler gabarito\n\t>>>> "+cl)

if(option == "2" or option == "02"):
    for i in range(3):
        chec(pes(url.text))
if(option == "1" or option == "01"):
    enviar()
if(option != "1" and option != "01" and option != "02" and option != "2"):
    print(red+"\n\tESCOLHA INVÁLIDA"+cl)
