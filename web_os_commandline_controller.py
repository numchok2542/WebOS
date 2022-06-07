from pywebostv.discovery import *
from pywebostv.connection import *
from pywebostv.controls import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import logging
import keyboard
import time
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
def power_clicked():
    #self.label.setText("Mute")
    #connecttv()
    system.power_off()
def appselector(appname):
    apps = app.list_apps()
    NF = [x for x in apps if appname in x["title"]][0]
    #Aprint(NF)
    launch_info = app.launch(NF)
    #print(launch_info)
    #time.sleep(10)
    #app.close(launch_info)
def pckeyboard(pcinp):
    inp.type(pcinp) # This sends keystrokes, but needs the
    keyboard to # be displayed
    on the screen.
    inp.enter()
    inp.delete(10)
    store = {'client_key': '34d56b27afa43b3cedd3f42bb78a0922'}
    # Scans the current network to discover TV. Avoid [0] in real code. If you
    already know the IP,
    webos_client = WebOSClient("192.168.1.10")
    webos_client.connect()
    for status in webos_client.register(store):
        if status == WebOSClient.PROMPTED:
            print("Please accept the connect on the TV!")
        elif status == WebOSClient.REGISTERED:
            print("Registration successful!")
# Keep the 'store' object because it contains now the access token
# and use it next time you want to register on the TV.
print(store) # {'client_key': 'ACCESS_TOKEN_FROM_TV'}
app = ApplicationControl(webos_client) #App
media = MediaControl(webos_client) #Volume
system = SystemControl(webos_client) #Turn off TV
inp = InputControl(webos_client) #Keyboard
tv_control = TvControl(webos_client) #TV channel
while(True):
    print("Available options:")
    print("App")
    print("Media")
    print("Keyboard")
    print("Notification")
    keyinp = input("Please select: ")
    #apps = app.list_apps()
    #print(apps)
    if keyinp == "Media":
        volinp = input("Please enter 1 to incrase vol, 2 to decrease, x to
        exit: ")
        while(volinp!="x"):
            if volinp=="1":
                media.volume_up()
                volinp = input("Please enter 1 to incrase vol, 2 to decrease, x
                to exit: ")
            if volinp=="2":
                media.volume_down()
                volinp = input("Please enter 1 to incrase vol, 2 to decrease, x
                to exit: ")
            if volinp=="m":
                if media.mute(True):
                    media.mute(False)
                else:
                    media.mute(True)
                else:
                continue
    if keyinp == "keyboard":
        pcinp=input("Please type (Make sure the keyboard is shown): ")
        while(pcinp!="x"):
            pckeyboard(pcinp)
            pcinp=input("Please type (Make sure the keyboard is shown): ")
    if keyinp=="App":
        apps = app.list_apps()
        print(apps)
        appinp = input("Please select the app: ")
        while(appinp!="x"):
            appselector(appinp)
            appinp = input("Please select the app: ")
    if keyinp=="Noti":
        notiinput = input("Please Enter the message: ")
        while(notiinput!="x"):
            system.notify(notiinput)
            notiinput = input("Please Enter the message: ")
