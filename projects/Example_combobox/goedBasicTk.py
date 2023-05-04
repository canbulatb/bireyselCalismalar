import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

import xlrd
import os
import sys
from gtts import gTTS
from playsound import playsound
import random
from PyQt5 import QtCore, QtGui, QtWidgets

pathGbFiles="nt2Tc01"
lesRandom=False
index=0
dirPath = os.path.dirname(os.path.realpath(__file__))
print(dirPath)
#print(sys.argv[0]) #çalışan py dosyasının yolunu gösteriyor. 
os.chdir(dirPath) # çalışma dizini olarak bu py dosyasının yeri seçiliyor. 
# Give the location of the file
dirPath=dirPath.replace("\\","/")
locDrs=dirPath+"/files/"+pathGbFiles+"/"
loc = dirPath+"/files/"+pathGbFiles+"/"+pathGbFiles+".xlsx"
# To open Workbook
print(loc)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name("01")

def pathEdit(klasor):
    global loc
    global locDrs
    locDrs=dirPath+"/files/"+klasor+"/"
    loc = dirPath+"/files/"+klasor+"/"+klasor+".xlsx"
   
    
    



def btnOk_click():
    soundPlay()

def soundPlay():
        global index
        global sheet
        global wb
        global lesRandom
        global locDrs
        global pathGbFiles

        #locDrs="./files/"+pathGbFiles+"/"
        fileLng2=locDrs+str(index)+"Nl.mp3"
        fileLng1=locDrs+str(index)+"Tr.mp3"
        #fileLng1="./files/"+pathGbFiles+"/"+str(index)+"Tr.mp3"
        #fileLng2="./files/"+pathGbFiles+"/"+str(index)+"Nl.mp3"
        


        answer=metin1.get()
        answer=answer.lower()
        answerS=sheet.cell_value(index,2).lower()
        print("answer"+str(answer))
        if answer==answerS:
            label3.config(text="Goed Bezik")
            print("Goed Bazig")
            playsound(fileLng2)            
            sonuc=True
            if lesRandom==True:
                index=random.randint(1,sheet.nrows)
            else:
                index+=1
            label3.config(text="")
            label1.config(text=sheet.cell_value(index,1))
            label2.config(text="")
            #self.edtSchriven.setText("")
            fileLng1=locDrs+str(index)+"Tr.mp3"
            #file=file.replace("gB.py","")
           
            cik=False
            while cik!=True:
                try:    
                    playsound(fileLng1)
                    cik=True
                except :  
                    soundMake(loc,locDrs)
        elif answer=="":
                label1.config(text=sheet.cell_value(index,1))
                label2.config(text="")
                label3.config(text="")
                metin1.config(text="")
                fileLng1=locDrs+str(index)+"Tr.mp3"
                cik=False
                while cik!=True:
                    try:    
                        playsound(fileLng1)
                        cik=True
                    except :  
                        soundMake(loc,locDrs)
               
        else:    
            fileLng2=locDrs+str(index)+"Nl.mp3"
            label2.config(text=sheet.cell_value(index,2))
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




# bind the selected value changes
def month_changed(event):
    global index
    global sheet
    global wb
    global lesRandom
    global loc
    global locDrs
    global pathGbFiles
    
    try:
        wb.close()
    except:
        pass   
    #self.qlabel.adjustSize()
    pathGbFiles=selected_gb.get()
    pathEdit(pathGbFiles)

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_name("01")
    
    label1.config(text=sheet.cell_value(index,1))
    label2.config(text="")

    index=0
    soundPlay()

    
    """ handle the month changed event """
    # showinfo(
    #     title='Result',
    #     message=f'You selected {selected_gb.get()}!'
    # )











root = tk.Tk()

img = tk.PhotoImage(file='C:\VIT Projesi\projects\Example_combobox\goedBezig.png')
width, height = img.width(), img.height()
logo = tk.Canvas(root, width=width, height=height)
logo.pack(fill=tk.X, padx=5, pady=5)
logo.create_image((1, 1), image=img, anchor="nw")

            


# config the root window
root.geometry('500x500')
#root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Çalışmak istediğiniz dersi seçiniz")
label.pack(fill=tk.X, padx=5, pady=5)
# create a combobox
selected_gb = tk.StringVar()
goedBezigCb = ttk.Combobox(root, textvariable=selected_gb)
filesDir=dirPath+"\\files\\"
p=os.listdir(dirPath+"\\files\\")
# get first 3 letters of every month name
goedBezigCb['values'] = [i for i in p if os.path.isdir(filesDir+i)]
# prevent typing a value
goedBezigCb['state'] = 'readonly'
# place the widget
goedBezigCb.pack(fill=tk.X, padx=5, pady=5)


label1_gb = tk.StringVar()
label1 = ttk.Label(root, textvariable=label1_gb)
label1 = ttk.Label(text="Çalışılacak text burada yazılacak.")
label1.pack(fill=tk.X, padx=5, pady=5)

label2_gb = tk.StringVar()
label2 = ttk.Label(root, textvariable=label2_gb)
label2 = ttk.Label(text="Çalışılacak text burada yazılacak.")
label2.pack(fill=tk.X, padx=5, pady=5)

metin1_gb = tk.StringVar()
metin1 = ttk.Entry(root, textvariable=metin1_gb)
metin1.pack(fill=tk.X, padx=5, pady=5)

# btn_gb = tk.StringVar()
btn = ttk.Button(root, text="Kontol et")
btn.config(command=btnOk_click)
btn.pack(fill=tk.X, padx=5, pady=5)


label3_gb = tk.StringVar()
label3 = ttk.Label(root, textvariable=label3_gb)
label3 = ttk.Label(text="Çalışılacak text burada yazılacak.")
label3.pack(fill=tk.X, padx=5, pady=5)




goedBezigCb.bind('<<ComboboxSelected>>', month_changed)


root.mainloop()