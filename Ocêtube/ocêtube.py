#coding: utf-8
#autor__Kaio Fábio Prates
from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm
import subprocess  as sp
import os
#colors
neg = '\033[1m';cl= '\033[0;0m';red= '\033[31m';green = '\033[32m'
blue = '\033[34m';cian = '\033[36m';mag = '\033[35m'
#funcion
def click(x):
    r = str(x)
    link = x
    YouTube(link).streams.first().download()

def clickp(x):
	pl=Playlist(x)
	pl.download_all()

def menu():
    print('\033[40;1;39m---Copie o link do video/Playlist do Youtube---\033[0;0m')
    print(blue+'01 - para Video\n02 - para Playlist'+cl)
    status, link = sp.getstatusoutput("termux-clipboard-get")
    es = input(green+'>>>'+cl)
    a  = range(1)
    #choice
    if (es == '01' or es == '1'):
        for i in tqdm(a):
            click(link)
    if (es == '02' or es == '2'):
        for i in tqdm(a):
            clickp(link)

#headers
print(red+'{:=^45}\n'.format(''))
print('   _ \\         /\\\\   |           |           \n  |   |   __|   _ \\  __|  |   |  __ \\    _ \\ \n  |   |  (      __/  |    |   |  |   |   __/ \n \\___/  \\___| \\___| \\__| \\__,_| _.__/  \\___| \n                                             \n')
print('{:=^45}'.format('kailp_may/2018'))
menu()
os.system('termux-notification -c "Video Baixado com SUCESSO" -t Ocêtube')
os.system('termux-toast -s "Video Baixado com Sucesso" ')
