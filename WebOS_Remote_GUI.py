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
# 1. For the first run, pass in an empty dictionary object. Empty store leads to an Authentication prompt on TV.
# 2. Go through the registration process. `store` gets populated in the process.
# 3. Persist the `store` state to disk.
# 4. For later runs, read your storage and restore the value of `store`.
#if your_custom_storage_is_empty():
  #  store = {}
#else:
  #  store = load_from_your_custom_storage()
 
class connection:
    def __init__(self,store,webos_client):
      self.store = store
      # Scans the current network to discover TV. Avoid [0] in real code. If you already know the IP,
      # you could skip the slow scan and # instead simply say:
      #    client = WebOSClient("<IP Address of TV>")
      #client = WebOSClient.discover()[0]
      self.webos_client = webos_client
      self.webos_client.connect()
      for status in self.webos_client.register(self.store):
          if status == self.webos_client.PROMPTED:
              print("Please accept the connect on the TV!")
          elif status == self.webos_client.REGISTERED:
              print("Registration successful!")
 
      # Keep the 'store' object because it contains now the access token
      # and use it next time you want to register on the TV.
      #print(self.store)   # {'client_key': 'ACCESS_TOKEN_FROM_TV'}
 
      
        
 
 
class MyWindow(QMainWindow):
    def __init__(self):
            
        super(MyWindow,self).__init__()
        self.initUI()
    def connecttv(self):
      self.conn = connection({'client_key': '34d56b27afa43b3cedd3f42bb78a0922'},WebOSClient("192.168.1.10"))
      # Scans the current network to discover TV. Avoid [0] in real code. If you already know the IP,
      # you could skip the slow scan and # instead simply say:
      #    client = WebOSClient("<IP Address of TV>")
      #client = WebOSClient.discover()[0]
      #self.webos_client = WebOSClient("192.168.1.10")
      #self.webos_client.connect()
      #for status in self.webos_client.register(self.store):
      #    if status == WebOSClient.PROMPTED:
      #        print("Please accept the connect on the TV!")
      #    elif status == WebOSClient.REGISTERED:
      #        print("Registration successful!")
 
      # Keep the 'store' object because it contains now the access token
      # and use it next time you want to register on the TV.
      print(self.conn.store)   # {'client_key': 'ACCESS_TOKEN_FROM_TV'}
 
      self.app = ApplicationControl(self.conn.webos_client) #App
      self.media = MediaControl(self.conn.webos_client) #Volume
      self.system = SystemControl(self.conn.webos_client) #Turn off TV
      self.inp = InputControl(self.conn.webos_client) #Keyboard
      self.tv_control = TvControl(self.conn.webos_client) #TV channel
      self.source_control = SourceControl(self.conn.webos_client)
 
 
 
    def one_clicked(self):
        self.label.setText("1")
        self.connecttv()
        #self.webosclient.launch_app(self.appid("tv"))
        apps = self.app.list_apps()
        print(apps)
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        #print(NF)
        launch_info = self.app.launch(NF)
 
 
    def two_clicked(self):
        self.label.setText("2")
        self.connecttv()
        apps = self.app.list_apps()
        print(apps)
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
 
    def three_clicked(self):
        self.label.setText("3")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
        self.tv_control.channel_down()
 
    def four_clicked(self):
        self.label.setText("4")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
 
    def five_clicked(self):
        self.label.setText("5")
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
       
 
    def six_clicked(self):
        self.label.setText("6")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
 
 
    def seven_clicked(self):
        self.label.setText("7")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
 
 
    def eight_clicked(self):
        self.label.setText("8")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
 
    def nine_clicked(self):
        self.label.setText("9")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
        self.tv_control.channel_down()
 
 
    def zero_clicked(self):
        self.label.setText("0")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Live TV" in x["title"]][0]
        print(NF)
 
  
        
    def list_clicked(self):
        self.label.setText("List")
        self.connecttv()
        #self.webos_client.launch_app(self.appid("list"))
        #self.update()
        apps = self.app.list_apps()
        print(apps)
 
    def guide_clicked(self):
        self.label.setText("Guide")
        self.connecttv()
        #self.webos_client.launch_app(self.appid("guide"))
        #self.update()
        apps = self.app.list_apps()
        NF = [x for x in apps if "ข้อมูล TV" in x["title"]][0]
        print(NF)
        launch_info = self.app.launch(NF)
 
    def netflix_clicked(self):
        self.label.setText("Netflix")
        self.connecttv()
        apps = self.app.list_apps()
        #apps = app.list_apps() 
        #self.webos_client.launch_app(self.appid("netflix"))
        #self.update()
        NF = [x for x in apps if "Netflix" in x["title"]][0]
        print(NF)
        launch_info = self.app.launch(NF)
 
    def setting_clicked(self):
        self.label.setText("การตั้งค่า")
        self.connecttv()
        apps = self.app.list_apps()
        #apps = app.list_apps() 
        #self.webos_client.launch_app(self.appid("netflix"))
        #self.update()
        NF = [x for x in apps if "การตั้งค่า" in x["title"]][0]
        print(NF)
        launch_info = self.app.launch(NF)
 
    def home_clicked(self):
        self.label.setText("Home")
        self.connecttv()
        #self.webos_client.launch_app(self.appid("youtube"))
        #self.update()
        apps = self.app.list_apps()
        #apps = app.list_apps() 
        #self.webos_client.launch_app(self.appid("netflix"))
        #self.update()
        NF = [x for x in apps if "Home" in x["title"]][0]
        print(NF)
        launch_info = self.app.launch(NF)
 
    def twitch_clicked(self):
        self.label.setText("Twitch")
        self.connecttv()
       # self.webos_client.launch_app(self.appid("twitch"))
        #self.update()
        apps = self.app.list_apps()
        NF = [x for x in apps if "Twitch" in x["title"]][0]
        print(NF)
        launch_info = self.app.launch(NF)
    def volup_clicked(self):
        self.label.setText("Volume Up")
        self.connecttv()
        #self.webos_client.volume_up()
        self.media.volume_up()
        #self.update()
 
    def voldown_clicked(self):
        self.label.setText("Volume Down")
        self.connecttv()
        #self.webos_client.volume_down()
        #self.update()
        self.media.volume_down()
 
    def chup_clicked(self):
        self.label.setText("Channel Up")
        self.connecttv()
        #self.webos_client.channel_up()
        #self.update()
        self.tv_control.channel_up()
        #self.tv_control.get_current_channel()
 
 
 
    def chdown_clicked(self):
        self.label.setText("Channel Down")
        self.connecttv()
        #self.webos_client.channel_down()
        #self.update()
        self.tv_control.channel_down()
        #self.tv_control.get_current_channel()
 
    def mute_clicked(self):
        self.label.setText("Mute")
        self.connecttv()
        soundstat = self.media.get_volume()
        #print(soundstat)
        if soundstat["volumeStatus"]["muteStatus"] == False:
            self.media.mute(True)
        else:
            self.media.mute(False)
 
    def power_clicked(self):
        #self.label.setText("Mute")
        self.connecttv()
        self.system.power_off() 
 
    def appselector(self):
        stext = self.searchbar.text()
        print(stext)
        self.label.setText("Search")
        self.connecttv()
        apps = self.app.list_apps()
        NF = [x for x in apps if stext in x["title"]][0]
        #Aprint(NF)
        launch_info = self.app.launch(NF)
        #print(launch_info)
        #time.sleep(10)
        #app.close(launch_info)  
 
    def play_clicked(self):
        self.label.setText("Play")
        self.connecttv()
        self.media.play()
    
    def stop_clicked(self):
        self.label.setText("Stop")
        self.connecttv()
        self.media.stop()
 
    def pause_clicked(self):
        self.label.setText("Pause")
        self.connecttv()
        self.media.pause()
 
    def rewind_clicked(self):
        self.label.setText("Rewind")
        self.connecttv()
        self.media.rewind()
 
    def ff_clicked(self):
        self.label.setText("Fast Forward")
        self.connecttv()
        self.media.fast_forward()
 
    def browser_clicked(self):
        self.label.setText("เว็บเบราว์เซอร์")
        self.connecttv()
       # self.webos_client.launch_app(self.appid("twitch"))
        #self.update()
        apps = self.app.list_apps()
        NF = [x for x in apps if "เว็บเบราว์เซอร์" in x["title"]][0]
        print(NF)
        launch_info = self.app.launch(NF)
 
    def bsource_clicked(self):
        self.label.setText("Select Source")
        self.connecttv()
        sources = self.source_control.list_sources()    # Returns a list of InputSource instances.
        print(sources)
        app_id = self.app.get_current()  
        if "av" in app_id:
            apps = self.app.list_apps()
            NF = [x for x in apps if "คอมโพเนนต์" in x["title"]][0]
            launch_info = self.app.launch(NF)
            self.label.setText("คอมโพเนนต์")
        elif "component" in app_id:
            apps = self.app.list_apps()
            NF = [x for x in apps if "HDMI1" in x["title"]][0]
            launch_info = self.app.launch(NF)
            self.label.setText("HDMI1")
        elif "hdmi1" in app_id:
            apps = self.app.list_apps()
            NF = [x for x in apps if "HDMI2" in x["title"]][0]
            launch_info = self.app.launch(NF)
            self.label.setText("HDMI2")
        elif "hdmi2" in app_id:
            apps = self.app.list_apps()
            NF = [x for x in apps if "HDMI3" in x["title"]][0]
            launch_info = self.app.launch(NF)
            self.label.setText("HDMI3")
        elif "hdmi3" in app_id:
            apps = self.app.list_apps()
            NF = [x for x in apps if "AV" in x["title"]][0]
            launch_info = self.app.launch(NF)
            self.label.setText("AV")
        #print(app_id)
        #self.source_control.set_source(sources[0]) 
      
    # id:com.webos.app.livetv, netflix, doonung, lgtv-hbogoasia1, amazon, com.viu.tv, com.webos.app.notificationcenter, 
    # com.webos.app.remoteservice, com.webos.app.accessibility, com.webos.app.livemenu, com.webos.app.miracast
    # com.webos.app.scheduler, com.webos.app.recordings, com.webos.app.photovideo, com.webos.app.music, com.webos.app.btspeakerapp
    # com.webos.app.connectionwizard, com.webos.app.tvuserguide, com.webos.app.browser, com.xstars.app.aquarelax, com.webos.app.hdmi2
    # com.webos.app.hdmi3, spotify-beehive, youtube.leanback.v4, airplay, com.webos.app.discover, tv.twitch.tv.starshot.lg
    # com.apple.appletv
 
    def initUI(self):
        self.setGeometry(0, 0, 300, 1000)
        self.setWindowTitle("Remote")
        self.setStyleSheet("background-color: White")
 
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Status Label")
        self.label.move(100,900)
 
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(0,0,90,90)
        self.b1.setText("1")
        self.b1.setFont(QFont('Ariel', 30))
        self.b1.clicked.connect(self.one_clicked)
 
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setGeometry(100,0,90,90)
        self.b2.setText("2")
        self.b2.setFont(QFont('Ariel', 30))
        self.b2.clicked.connect(self.two_clicked)
 
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setGeometry(200,0,90,90)
        self.b3.setText("3")
        self.b3.setFont(QFont('Ariel', 30))
        #self.b3.setStyleSheet("background-color: black")
        self.b3.clicked.connect(self.three_clicked)
 
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setGeometry(0,100,90,90)
        self.b4.setText("4")
        self.b4.setFont(QFont('Ariel', 30))
        self.b4.clicked.connect(self.four_clicked)
 
        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setGeometry(100,100,90,90)
        self.b5.setText("5")
        self.b5.setFont(QFont('Ariel', 30))
        self.b5.clicked.connect(self.five_clicked)
 
        self.b6 = QtWidgets.QPushButton(self)
        self.b6.setGeometry(200,100,90,90)
        self.b6.setText("6")
        self.b6.setFont(QFont('Ariel', 30))
        self.b6.clicked.connect(self.six_clicked)
 
        self.b7 = QtWidgets.QPushButton(self)
        self.b7.setGeometry(0,200,90,90)
        self.b7.setText("7")
        self.b7.setFont(QFont('Ariel', 30))
        self.b7.clicked.connect(self.seven_clicked)
 
        self.b8 = QtWidgets.QPushButton(self)
        self.b8.setGeometry(100,200,90,90)
        self.b8.setText("8")
        self.b8.setFont(QFont('Ariel', 30))
        self.b8.clicked.connect(self.eight_clicked)
 
        self.b9 = QtWidgets.QPushButton(self)
        self.b9.setGeometry(200,200,90,90)
        self.b9.setText("9")
        self.b9.setFont(QFont('Ariel', 30))
        self.b9.clicked.connect(self.nine_clicked)
 
        self.blist = QtWidgets.QPushButton(self)
        self.blist.setGeometry(0,300,90,90)
        self.blist.setText("List")
        self.blist.setFont(QFont('Ariel', 20))
        self.blist.clicked.connect(self.list_clicked)
 
        self.b0 = QtWidgets.QPushButton(self)
        self.b0.setGeometry(100,300,90,90)
        self.b0.setText("0")
        self.b0.setFont(QFont('Ariel', 30))
        self.b0.clicked.connect(self.zero_clicked)
 
        self.bguide = QtWidgets.QPushButton(self)
        self.bguide.setGeometry(200,300,90,90)
        self.bguide.setText("Guide")
        self.bguide.setFont(QFont('Ariel', 20))
        self.bguide.clicked.connect(self.guide_clicked)
 
        self.chlabel = QtWidgets.QLabel(self)
        self.chlabel.setText("Channel")
        self.chlabel.setFont(QFont('Ariel', 12))
        self.chlabel.move(200,770)
 
        self.vollabel = QtWidgets.QLabel(self)
        self.vollabel.setText("Volume")
        self.vollabel.setFont(QFont('Ariel', 12))
        self.vollabel.move(0,770)
 
        self.bvolup = QtWidgets.QPushButton(self)
        self.bvolup.setGeometry(0,800,70,50)
        #self.bvolup.setText("volup")
        #self.bvolup.setFont(QFont('Ariel', 12))
        self.bvolup.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/volup.jpg);")
        self.bvolup.clicked.connect(self.volup_clicked)
 
        self.bvoldown = QtWidgets.QPushButton(self)
        self.bvoldown.setGeometry(0,860,70,50)
        #self.bvoldown.setText("voldown")
        #self.bvoldown.setFont(QFont('Ariel', 12))
        self.bvoldown.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/voldown.jpg);")
        self.bvoldown.clicked.connect(self.voldown_clicked)
 
        self.bchup = QtWidgets.QPushButton(self)
        self.bchup.setGeometry(200,800,70,50)
        #self.bchup.setText("chup")
        #self.bchup.setFont(QFont('Ariel', 12))
        self.bchup.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/up.jpg);")
        self.bchup.clicked.connect(self.chup_clicked)
 
        self.bchdown = QtWidgets.QPushButton(self)
        self.bchdown.setGeometry(200,860,70,50)
       # self.bchdown.setText("chdown")
        #self.bchdown.setFont(QFont('Ariel', 12))
        self.bchdown.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/down.jpg);")
        self.bchdown.clicked.connect(self.chdown_clicked)
 
        self.bnetflix = QtWidgets.QPushButton(self)
        self.bnetflix.setGeometry(0,400,90,90)
        self.bnetflix.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/adjnetflix.png);")
        self.bnetflix.clicked.connect(self.netflix_clicked)
 
        self.bsettings = QtWidgets.QPushButton(self)
        self.bsettings.setGeometry(0,500,90,90)
        self.bsettings.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/setting.jpg);")
        self.bsettings.clicked.connect(self.setting_clicked)
 
        self.bhome = QtWidgets.QPushButton(self)
        self.bhome.setGeometry(100,400,90,90)
        self.bhome.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/Homeadj.jpg);")
        self.bhome.clicked.connect(self.home_clicked)
 
        self.btwitch = QtWidgets.QPushButton(self)
        self.btwitch.setGeometry(200,400,90,90)
        self.btwitch.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/adjtwitch.png);")
        self.btwitch.clicked.connect(self.twitch_clicked)
 
        self.bmute = QtWidgets.QPushButton(self)
        self.bmute.setGeometry(200,500,90,90)
        self.bmute.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/mute.jpg);")
        self.bmute.clicked.connect(self.mute_clicked)
 
        self.bpower = QtWidgets.QPushButton(self)
        self.bpower.setGeometry(100,500,90,90)
        self.bpower.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/power.jpg);")
        self.bpower.clicked.connect(self.power_clicked)
 
        self.bbrowser = QtWidgets.QPushButton(self)
        self.bbrowser.setGeometry(000,600,90,90)
        self.bbrowser.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/browser.jpg);")
        self.bbrowser.clicked.connect(self.browser_clicked)
 
        self.searchbar = QtWidgets.QLineEdit(self)
        #self.searchbar.setText("")
        self.searchbar.setGeometry (100,600,100,50)
 
        self.bsearchyes = QtWidgets.QPushButton(self)
        self.bsearchyes.setGeometry(200,600,60,60)
        self.bsearchyes.setText("OK")
        self.bsearchyes.setFont(QFont('Ariel', 12))
        self.bsearchyes.clicked.connect(self.appselector)
        #self.bsearchyes.clicked.connect(self.appselector("Live TV"))
 
 
        self.bplay = QtWidgets.QPushButton(self)
        self.bplay.setGeometry(0,700,30,30)
        self.bplay.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/play.jpg);")
        self.bplay.clicked.connect(self.play_clicked)
 
        self.bstop = QtWidgets.QPushButton(self)
        self.bstop.setGeometry(32,700,30,30)
        self.bstop.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/stop.jpg);")
        self.bstop.clicked.connect(self.stop_clicked)
 
        self.bpause = QtWidgets.QPushButton(self)
        self.bpause.setGeometry(62,700,30,30)
        self.bpause.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/pause.jpg);")
        self.bpause.clicked.connect(self.pause_clicked)
 
        self.brewind = QtWidgets.QPushButton(self)
        self.brewind.setGeometry(92,700,30,30)
        self.brewind.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/rewind.jpg);")
        self.brewind.clicked.connect(self.rewind_clicked)
 
        self.bff = QtWidgets.QPushButton(self)
        self.bff.setGeometry(122,700,30,30)
        self.bff.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/ff.jpg);")
        self.bff.clicked.connect(self.ff_clicked)
 
        self.bsource = QtWidgets.QPushButton(self)
        self.bsource.setGeometry(200,700,60,60)
        self.bsource.setStyleSheet("background-image : url(C:/Users/GE63 8RF/Desktop/PyWebOSTV-master/PyWebOSTV-master/pywebostv/images/input.png);")
        self.bsource.clicked.connect(self.bsource_clicked)
 
        #self.bsearchyes.clicked.connect(self.appselector("Live TV"))
    def update(self):
        self.label.adjustSize()
    
    def pckeyboard(self,pcinp):
      self.inp.type(pcinp)            # This sends keystrokes, but needs the keyboard to                                                # be displayed on the screen.
      self.inp.enter()           
      self.inp.delete(10) 
 
def window():
        app = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec_())
window()
 
 
 
