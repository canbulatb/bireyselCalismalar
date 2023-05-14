import random
class banka:
    def __init__(self,adi,soyadi):
        self.__adi=adi
        self.__soyAdi=soyadi
        self.__hesapNumarasi=[]
        self.__hesapNumarasi.append('ABN' + f'{random.randint(1000000000,9999999999)}')
        self.__bakiye=[]
        self.__bakiye.append(0)
    
    def bakiye(self):

        for x in range(0,len(self.__hesapNumarasi)):
            print(f"Hesap Numarası      : {self.__hesapNumarasi[x]}")
            print(f"Bakiye              : {self.__bakiye[x]}")
        
    def adi(self):
        return self.__adi
    
    def soyAdi(self):
        return self.__soyAdi
    
    def hesapNumarasi(self):
        return self.__hesapNumarasi
    
    def paraYatir(self,aktifHesap,miktar):
        
        self.__bakiye[aktifHesap]+=miktar
        print(f"Para yatırıldı. Yeni bakiye { self.__bakiye[aktifHesap]}")
        
    def paraCek(self,aktifHesap,miktar):
        self.__bakiye[aktifHesap]-=miktar
        print(f"Para Çekildi. Yeni bakiye { self.__bakiye[aktifHesap]}")
        
    def yeniHesapEkle(self,sorma):
        if sorma==False:
            sor=input(f"{self.__adi} {self.__soyAdi} müşterisine yeni hesap açmak mı istiyorsunuz: (EVET)")
        else:
            sor="EVET"
        if sor=="EVET":
            self.__hesapNumarasi.append('ABN' + f'{random.randint(1000000000,9999999999)}')
            self.__bakiye.append(0)
            print(f"{self.__adi} {self.__soyAdi} müşterisine yeni hesap açıldı.")
        else:
            input("Herhangi bir işlem yapılmadı...")
    
    def aktifHesabiSil(self,aktifHesap):
        if len(self.__hesapNumarasi)>1:
            print("Hesabı silmek istediğinizden emin misiniz?")
            cevap=input("(EVET)  : ")
            if cevap=="EVET":
                del self.__hesapNumarasi[aktifHesap]
                del self.__bakiye[aktifHesap]
                print("HESAP SİLİNDİ.....")
                input()
                if aktifHesap>0:
                    aktifHesap-=1
                
        else:
            print("TEK HESAP VAR. HESAP BURADAN KAPATILAMAZ. ")
            input()

        return aktifHesap   
        
    
    def hesapDegistir(self,aktifHesap):
        hesap=0
        yildiz=""
        
        while True:
            for x in range(0,len(self.__hesapNumarasi)):
                if x==aktifHesap:
                    yildiz="*"
                else:
                    yildiz=""
                print(x,"-",self.__hesapNumarasi[x]," Bakiye:",self.__bakiye[x],yildiz )

            hesap=input(f"Lütfen bir hesabı seçin 0-{x} ")
            if hesap in "0123456789" and len(hesap)==1 and int(hesap)<=x:
                break
        return int(hesap)
    
    def toplamBakiye(self,aktifHesap):
        toplamBakiye=0
        for x in range(0,len(self.__hesapNumarasi)):
            if x==aktifHesap:
                yildiz="*"
            else:
                yildiz=""
            print(x,"-",self.__hesapNumarasi[x]," Bakiye:",self.__bakiye[x],yildiz )
            toplamBakiye+=self.__bakiye[x]
        print(f"Toplam Bakiye = {toplamBakiye}")
    
    
                


        
        