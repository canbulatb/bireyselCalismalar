from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import xlrd
import os
import sys
from gtts import gTTS
from playsound import playsound

class Program(App):
    def build(self):
        self.anaDuzen = BoxLayout(orientation = "vertical") # Elemanların hepsini tutan ana pencere düzenimiz
        self.ilkSatir = BoxLayout()
        self.ikinciSatir = BoxLayout()
        self.nick = Label(text = "Nick")
        self.nickKutu = TextInput(multiline = False)
        self.sifre = Label(text = "Şifre")
        self.sifreKutu = TextInput(multiline = False,
                              password = True,
                              password_mask = "?")

        self.buton = Button(text = "Giriş Yap")
        self.buton.bind(on_press = self.kontrol) # Butonumuza tıklama olayı ekledik


        self.ilkSatir.add_widget(self.nick)
        self.ilkSatir.add_widget(self.nickKutu)

        self.ikinciSatir.add_widget(self.sifre)
        self.ikinciSatir.add_widget(self.sifreKutu)

        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)
        self.anaDuzen.add_widget(self.buton)

        return self.anaDuzen

    def kontrol(self,event = None):
        print(sys.argv[0]) #çalışan py dosyasının yolunu gösteriyor. 
        os.chdir((os.path.dirname(sys.argv[0]))) # çalışma dizini olarak bu py dosyasının yeri seçiliyor. 
        # Give the location of the file
        loc = (os.path.dirname(sys.argv[0]) + "/files/data/les01Tr-Nl.xlsx")
        # To open Workbook
        #print(loc)
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_name("01")
        
        index=1
        while True:
            self.buton.text=""
            self.nick.text=sheet.cell_value(index,1)
            print(sheet.cell_value(index,1))
            file=sys.argv[0] + "/files/sound/"+str(index)+"Tr.mp3"
            file=file.replace("kivytest.py","")
            playsound(file)
            answer=self.nickKutu.text
            if answer=="":
                break
            if answer==sheet.cell_value(index,2):
                self.buton.text="Goed Bazig"
                print("Goed Bazig")
                index+=1
                file=sys.argv[0] + "/files/sound/"+str(index-1)+"Nl.mp3"
                file=file.replace("kivytest.py","")
                playsound(file)
            else:
                file=sys.argv[0] + "/files/sound/"+str(index)+"Nl.mp3"
                file=file.replace("kivytest.py","")
                self.sifre.text=sheet.cell_value(index,2)
                print(sheet.cell_value(index,2))
                playsound(file)
                
    
        
        
Program().run()