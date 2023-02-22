from turtle import clear
import psutil as ps
import os
import time
import win32com.client as win32
import subprocess
i=0

while(i==0):
        b=0
        a=0
        c=0

        #print('Lista de processos em execução:')
        for proc in ps.process_iter():

            info = proc.as_dict(attrs=['pid', 'name'])
            #print('Processo: {} (PID: {})'.format(info['pid'], info['name']))
            if(info['name']=="Zoom.exe"):
                print("ZOOM EXECUTANDO!!!")
                a=a+1

            if(info['name']=="AnyDesk.exe"):
                print("ANYDESK EXECUTANDO!!!")
                b=b+1

            if(info['name']=="VirtualBox.exe"):
                print("VIRTUAL BOX EXECUTANDO!")

                c=c+1
                time.sleep(0.5)
                os.system("cls")

        if(a==0 or b==0 or c==0):

                print("INICIANDO PROGRAMA!!!")
                time.sleep(2)
                if(a == 0) : os.system("start C:\\Users\\felip\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
                if(b == 0):os.system("start C:\\progra~2\\AnyDesk\\AnyDesk.exe")
                if(c == 0): os.system("start C:\\progra~1\\Oracle\\VirtualBox\\VirtualBox.exe")

