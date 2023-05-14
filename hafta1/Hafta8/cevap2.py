from banka import *
musteriler=[]
global aktifMusteri
aktifMusteri=0
aktifHesap=0
        
def musteriSec():
    global aktifMusteri
    adi=input("Lütfen müşterinin adını giriniz...:")
    indexNo=0        
    for x in musteriler:
        if x.adi()==adi:
            print(x.adi(),x.soyAdi(),"Aradığınız müşteri bu mu?")
            cevap=input("E/H")
            if cevap in "Ee" and len(cevap)==1:
                aktifMusteri=indexNo
                break
            else:
                indexNo+=1
        else:
            indexNo+=1
    if cevap not in "Ee":
        input("Aradığınız müşteri bulunamadı.")            

def hesapOlustur():
    print("Lütfen hesap sahibinin : \n")
    adi=input("Adını giriniz: ")
    soyadi=input("Soyadını giriniz: ")
    musteriler.append(banka(adi,soyadi))

def listele():
    for x in musteriler:
        print(f"Müşterinin Adı    :{x.adi()}")
        print(f"Müşterinin Soyadı :{x.soyAdi()}")
        x.bakiye()
        print("*"*30)
    input()

def anaMenu():
    while True:
        print(" Bankacılık sistemine hoş geldiniz!")
        print("Aktif Müşteri", musteriler[aktifMusteri].adi())
        print("""
            1-Musteri Seç
            2-Muşteri İşlemleri
            3-Muşterileri Listele
            4-Müşteri Hesabı Sil
            5-Yeni Müşteri Oluştur
            Q-Programdan Çıkış""")
        secenek=input("Lütfen bir seçenek seçin : ").upper()
        if secenek in "12345Qq" and len(secenek)==1:
            break
        else:
            print("HATALI GİRİŞ YAPTINIZ... LÜTFEN SEÇENEKLERDEN BİRİNİ GİRİNİZ..." )
            print("*"*30)
    return secenek
        
def musteriMenu():
    while True:
        print("Aktif Müşteri", musteriler[aktifMusteri].adi())
        print("""Bankacılık sistemine hoş geldiniz!
            1-Hesap oluştur
            2-Para yatırma
            3-Para çekme
            4-Hesap kaldırma
            5-Toplam bakiye sorgulama
            6-Diğer hesaba geç
            Q-Muşteriden Çıkış""")
        secenek=input("Lütfen bir seçenek seçin").upper()
        if secenek in "123456Qq" and len(secenek)==1:
            break
        else:
            print("HATALI GİRİŞ YAPTINIZ... LÜTFEN SEÇENEKLERDEN BİRİNİ GİRİNİZ..." )
            print("*"*30)
    return secenek

def hesabiSil():
    global aktifMusteri
    print("Hesabı silmek istediğinizden emin misiniz?")
    print(musteriler[aktifMusteri].adi())
    print(musteriler[aktifMusteri].soyAdi())
    cevap=input("(EVET)  : ")
    if cevap=="EVET":
        del musteriler[aktifMusteri]
        print("HESAP SİLİNDİ.....")
        if aktifMusteri>0:
            aktifMusteri-=1
        input()
    else:
        print("İşlem Yapılmadı.")
        input()


musteriler.append(banka("Bilal","Can"))
musteriler.append(banka("Fatma","Canb"))
musteriler[0].yeniHesapEkle(True)
musteriler[1].yeniHesapEkle(True)

while True:
    anaMenuSecim=anaMenu()
    if anaMenuSecim=="1":
        musteriSec()
    elif anaMenuSecim=="2":
        #********************************* MÜŞTERİ MENU SEÇENEKLERİ
        while True:
            secim=musteriMenu() 
            if secim=="1":
                musteriler[aktifMusteri].yeniHesapEkle(False)
            elif secim=="2":
                while True:
                    try:
                        paraYatir=int(input("Yatırılacak miktarı giriniz...: ")) #Şimdilik integer girişe izin veriliyor...
                        break
                    except:
                        print("Yanlış giriş yaptınız. Lütfen miktarı giriniz...:")   
                musteriler[aktifMusteri].paraYatir(aktifHesap,paraYatir)
            elif secim=="3":
                while True:
                    try:
                        paraCek=int(input("Çekilecek miktarı giriniz...: ")) #Şimdilik integer girişe izin veriliyor...
                        break
                    except:
                        print("Yanlış giriş yaptınız. Lütfen miktarı giriniz...:")   
                musteriler[aktifMusteri].paraCek(aktifHesap,paraCek)
            elif secim=="4":
                #Hesap Kaldırma
                aktifHesap=musteriler[aktifMusteri].aktifHesabiSil(aktifHesap)
                 

                pass
            elif secim=="5":
                #Toplam bakiye sorgulama
                musteriler[aktifMusteri].toplamBakiye(aktifHesap)
                pass
            elif secim=="6":
                aktifHesap=musteriler[aktifMusteri].hesapDegistir(aktifHesap)
            elif secim in "Qq":
                break
        #********************************* MÜŞTERİ MENU SEÇENEKLERİ SONU
    elif anaMenuSecim=="3":
        listele()
    elif anaMenuSecim=="4":
        hesabiSil()
        #müşteri hesabı sil
    elif anaMenuSecim=="5":
        hesapOlustur()
    elif anaMenuSecim=="Q":
        break
        
    