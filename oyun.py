import random

#kullanıcı seçimini ve oyun istatistiği için oluşturulan listeler.
gameData={"T":"Taş", "K":"Kağıt", "M":"Makas"}
gameDataCount={"U":0, "C":0, "E":0}
gameDataL=["Taş", "Kağıt", "Makas"]

#Kullanıcının belirlenen tuşlara basarak ilerlemesini sağlamak için oluşturulan liste
choiceL=["T","K","M","t","k","m","Q","q"] 

userName= input("Lütfen Adınızı Giriniz :")
print(f"Merhaba {userName}")
print("Taş - Kağıt - Makas Oyunumuza Hoşgeldiniz...")


while True:    
    while True:
        userChoice=input("Lütfen (T)aş - (K)ağıt - (M)akas tan birini seçiniz... (T/K/M) \n Çıkış için Q tuşuna Basınız... ")
        #eğer kullanıcının bastığı tuş, istenilen tuşlardan biri ise döngüden çıkıyor.
        if userChoice in choiceL:  
            break
        else: print("Lütfen sadece belirtilen tuşlardan birine basınız...(T/K/M - Çıkış -Q)")

    #eğer Q tuşuna basılmış ise ana döngüden çıkış yapıyor.(Oyundan çıkış)     
    if userChoice.upper()=="Q": 
        break
    
    #kullanıcının seçimi Taş, Kağıt veya Makas olarak değişkene aktarılıyor.  
    userChoiceEnd=gameData[userChoice.upper()]
    #Bilgisayarın seçimi aktarılıyor. 
    botChoice=random.choice(gameDataL)
    
    #Kullanıcı ve Bilgisayarın seçimleri yazdırılıyor.
    print(f"Kullanıcı Seçimi \a{userChoiceEnd} ve Bilgisayar Seçimi {botChoice}")
    
    #kimin kazandığı belirleniyor. 
    if userChoiceEnd=="Taş":
        if botChoice=="Makas":
            whoWin="\nTaş Makası Kırar, \n Tebrikler Sen Kazandın...\n\n"
            gameDataCount["U"]+=1
        elif botChoice=="Kağıt":
            whoWin="\nKağıt Taşı Sarar, \n Üzgünüm Kaybettin....\n\n"
            gameDataCount["C"]+=1
        else: 
            whoWin="\nBerabere Kaldınız...\n\n"
            gameDataCount["E"]+=1
    
    elif userChoiceEnd=="Kağıt":
        if botChoice=="Makas":
            whoWin="\nMakası kağıdı keser, \n Üzgünüm Kaybettin....\n\n"
            gameDataCount["C"]+=1
        elif botChoice=="Taş":
            whoWin="\nKağıt Taşı Sarar \n Tebrikler Sen Kazandın...\n\n"
            gameDataCount["U"]+=1
        else: 
            whoWin="\nBerabere Kaldınız...\n\n"
            gameDataCount["E"]+=1
    
    elif userChoiceEnd=="Makas":
        if botChoice=="Kağıt":
            whoWin="\nMakası kağıdı keser, \n Tebrikler Sen Kazandın...\n\n"
            gameDataCount["U"]+=1
        elif botChoice=="Taş":
            whoWin="\nTaş Makası kırar, \n Üzgünüm Kaybettin....\n\n"
            gameDataCount["C"]+=1
        else: 
            whoWin="\nBerabere Kaldınız...\n\n"
            gameDataCount["E"]+=1
            
    #Oyunun sonucu yazdırılıyor. 
    print(whoWin)
#Eğer oyun en az 1 defa oynanmışsa istatistikler yazdırılıyor. 
if gameDataCount['E']+gameDataCount['C']+gameDataCount['U']>0:
    print(f"Toplam {gameDataCount['E']+gameDataCount['C']+gameDataCount['U']} defa oyunu oynandınız.")
    print(f"{gameDataCount['U']} defa sen kazandın.\n{gameDataCount['C']} defa bilgisayar kazandı.")
    print(f"{gameDataCount['E']} defa berabere kaldınız.")
    if gameDataCount["U"]>gameDataCount["C"]:
        print(f"Tebrikler {userName}... Çok iyi oyun oynadın...")
    elif gameDataCount["U"]==gameDataCount["C"]:
        print(f"Az daha kazanıyordun {userName}. İyi iş çıkardın...")
    else:
        print(f"{userName} çok üzgünüm. Bir dahaki sefere daha iyi olabilir...")

print("Hoşçakal. Tekrar görüşmek üzere...")    
    
