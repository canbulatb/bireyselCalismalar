import xlrd
import os
import sys
from gtts import gTTS
from playsound import playsound

print(sys.argv[0]) #çalışan py dosyasının yolunu gösteriyor. 
os.chdir((os.path.dirname(sys.argv[0]))) # çalışma dizini olarak bu py dosyasının yeri seçiliyor. 
# Give the location of the file
loc = (os.path.dirname(sys.argv[0]) + "/files/data/les01Tr-Nl.xlsx")
# To open Workbook
print(loc)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name("01")

def soundMake():
    print(sys.argv[0]) #çalışan py dosyasının yolunu gösteriyor. 
    os.chdir((os.path.dirname(sys.argv[0]))) # çalışma dizini olarak bu py dosyasının yeri seçiliyor. 
    print ("SYSTEM PATH "+ os.path.dirname(sys.argv[0]))
    # Give the location of the file
    loc = (os.path.dirname(sys.argv[0]) + "/files/data/les01Tr-Nl.xlsx")
    # To open Workbook
    print(loc)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_name("01")
    for i in range(sheet.nrows):
            index = sheet.cell_value(i,0) #row[0]
            if index=="":
                break
            trWord = sheet.cell_value(i,1)
            trSound = gTTS(text=trWord, lang="tr", slow=False)
            trSound.save(os.path.dirname(sys.argv[0]) + "/files/sound/"+str(i)+"Tr.mp3")
            nlWord = sheet.cell_value(i,2)
            nlSound = gTTS(text=nlWord, lang="nl", slow=False)
            nlSound.save(os.path.dirname(sys.argv[0]) + "/files/sound/"+str(i)+"Nl.mp3")

index=1
while True:
    print(sheet.cell_value(index,1))
    file=sys.argv[0] + "/files/sound/"+str(index)+"Tr.mp3"
    file=file.replace("Goed Bezig.py","")
    playsound(file)
    answer=input()
    if answer=="":
        break
    if answer==sheet.cell_value(index,2):
        print("Goed Bazig")
        index+=1
        file=sys.argv[0] + "/files/sound/"+str(index-1)+"Nl.mp3"
        file=file.replace("Goed Bezig.py","")
        playsound(file)
        
    else:
        file=sys.argv[0] + "/files/sound/"+str(index)+"Nl.mp3"
        file=file.replace("Goed Bezig.py","")
        print(sheet.cell_value(index,2))
        playsound(file)
        
    