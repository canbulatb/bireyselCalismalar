# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goedBezikqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import xlrd
import os
import sys
from gtts import gTTS
from playsound import playsound
import random
from PyQt5 import QtCore, QtGui, QtWidgets

pathGbFiles="nt2Tc01"
lesRandom=False

index=1
dirPath = os.path.dirname(os.path.realpath(__file__))
print(dirPath)
#print(sys.argv[0]) #çalışan py dosyasının yolunu gösteriyor. 
os.chdir(dirPath) # çalışma dizini olarak bu py dosyasının yeri seçiliyor. 
# Give the location of the file
#dirPath=dirPath.replace("\\","/")
loc = dirPath+"\\files\\"+pathGbFiles+"\\"+pathGbFiles+".xlsx"
locDrs=dirPath+"\\files\\"+pathGbFiles+"\\"
# To open Workbook
print(loc)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name("01")

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.edtSchriven = QtWidgets.QLineEdit(Dialog)
        self.edtSchriven.setGeometry(QtCore.QRect(10, 110, 381, 20))
        self.edtSchriven.setObjectName("edtSchriven")
        self.lblSpreek = QtWidgets.QLabel(Dialog)
        self.lblSpreek.setGeometry(QtCore.QRect(10, 20, 381, 71))
        self.lblSpreek.setText("")
        
        self.lblSpreek2 = QtWidgets.QLabel(Dialog)
        self.lblSpreek2.setGeometry(QtCore.QRect(10, 40, 381, 71))
        self.lblSpreek2.setText("")
        
        self.lblSpreek.setObjectName("lblSpreek")
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(10, 150, 381, 23))
        self.btnOk.setObjectName("btnOk")
        self.lblGoedBezig = QtWidgets.QLabel(Dialog)
        self.lblGoedBezig.setGeometry(QtCore.QRect(20, 190, 381, 21))
        self.lblGoedBezig.setText("")
        self.lblGoedBezig.setObjectName("lblGoedBezig")
        self.btnOk.clicked.connect(self.btnOk_click)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnOk.setText(_translate("Dialog", "Controle"))
        self.lblSpreek.setText(sheet.cell_value(index,1))
        
    
    def btnOk_click(self):
        soundPlay(self)
    
    
     

def soundPlay(self):
        global index
        global sheet
        global wb
        global lesRandom

        answer=self.edtSchriven.text()
        print("answer"+str(answer))
        if answer==sheet.cell_value(index,2):
            self.lblGoedBezig.setText("Goed Bezik")
            print("Goed Bazig")            
            sonuc=True
            fileLng2=locDrs+str(index)+"Nl.mp3"
            #file=file.replace("gB.py","")
            playsound(fileLng2)
            if lesRandom==True:
                index=random.randint(1,sheet.nrows)
            else:
                index+=1
            self.lblGoedBezig.setText("")
            self.lblSpreek.setText(sheet.cell_value(index,1))
            self.lblSpreek2.setText("")
            self.edtSchriven.setText("")
            fileLng1=locDrs+str(index)+"tr.mp3"
            #file=file.replace("gB.py","")
            playsound(fileLng1)
        else:
            fileLng2=locDrs+str(index)+"Nl.mp3"
            self.lblSpreek2.setText(sheet.cell_value(index,2))
            print(sheet.cell_value(index,2))
            playsound(fileLng2)

def soundMake(locPath,savePath):
    print(sys.argv[0]) #çalışan py dosyasının yolunu gösteriyor. 
    os.chdir((os.path.dirname(sys.argv[0]))) # çalışma dizini olarak bu py dosyasının yeri seçiliyor. 
    print ("SYSTEM PATH "+ os.path.dirname(sys.argv[0]))
    # Give the location of the file
    #locPath = (os.path.dirname(sys.argv[0]) + "/files/data/les01Tr-Nl.xlsx")
    # To open Workbook
    print(locPath)
    wb = xlrd.open_workbook(locPath)
    sheet = wb.sheet_by_name("01")
    for i in range(sheet.nrows):
            index = sheet.cell_value(i,0) #row[0]
            if index=="":
                break
            trWord = sheet.cell_value(i,1)
            trSound = gTTS(text=trWord, lang="tr", slow=False)
            trSound.save(savePath+str(i)+"Tr.mp3")
            nlWord = sheet.cell_value(i,2)
            nlSound = gTTS(text=nlWord, lang="nl", slow=False)
            nlSound.save(savePath+str(i)+"Nl.mp3")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    cik=False
    while cik!=True:
        try:    
            fileLng2=locDrs+str(index)+"Tr.mp3"
            playsound(fileLng2)
            cik=True
        except :  
            soundMake(loc,locDrs)
    sys.exit(app.exec_())
