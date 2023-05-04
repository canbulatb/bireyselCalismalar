#     Telefon Rehberi Uygulaması
# Bu program, kullanıcıların telefon rehberlerindeki kişileri yönetmelerine ve aramalarına olanak tanır. Program, Python sözlüklerini kullanarak verileri depolar.

# Özellikler

# Yeni kişi ekleme
# Kişi düzenleme
# Kişi silme
# Kişi arama
# Fonksiyonlar
# Programınız aşağıdaki fonksiyonlardan oluşabilir:

# kişi_ekle()
# Bu fonksiyon, kullanıcıdan bir kişi adı ve telefon numarası alarak telefon rehberine ekler.

# kişi_düzenle()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur. Ardından, kullanıcıya mevcut verileri güncelleme veya silme seçenekleri sunar.

# kişi_sil()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve siler.

# kişi_arama()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve ekrana görüntüler.


#Bu fonksiyon yeni kişi eklemek için kullanıldı. 
def kisiEkle(liste):
    print("*"*10,"Kişi Ekleme","*"*10)
    adi=input("Adı : ")
    soyadi=input("Soyadi : ")
    telefonNo=input("Telefon No : ")
    liste.append([adi,soyadi,telefonNo])   
    input("Kişi Eklendi...")

#Bu fonksiyon arama yapmak için kullanıldı. Liste içerisinden aranan kayıtları bulur
#başka bir listeye kaydererek return yapar.Düzeltme ve silme işlemleri bu fonksiyonu kullanır.
def arama(liste):
    i=0
    sonucReturn=[]
    araIstek=input("Lütfen aramak istediğiniz bilgiyi giriniz:")
    for bilgi in (liste):
        for bilgi2 in bilgi:
            if araIstek in bilgi2:
                sonucReturn+=[i]
        i+=1
    return sonucReturn

#Kişi aramak için bu fonksiyon kullanılıyor. 
def kisiArama(liste):
    aramaYap=arama(liste)
    bulunduMu=False
    for lst in aramaYap:
        print(liste[lst])
        sonuc=input("İstediğiniz kayda ulaşabildiniz mi? (E/H)")
        if sonuc in "Ee":
            bulunduMu=True
            break
    if bulunduMu==False:
        print("Üzgünüm Aradığınız kişi bizde kayıtlı değil...")

#Bilgi girişi için bu fonksiyon kullanılıyor.
def bilgiGir():
    adi=input("Adı : ")
    soyadi=input("Soyadi : ")
    telefonNo=input("Telefon No : ")
    return [adi, soyadi,telefonNo]    
    
    
#kişi düzeltmek için bu fonksiyon kullanılıyor. 
def kisiDuzeltme(liste):
    aramaYap=arama(liste)
    bulunduMu=False
    for lst in aramaYap:
        print(liste[lst])
        sonuc=input("Düzeltmek istediğiniz kayıt bu mu? (E/H)")
        if sonuc in "Ee":
            bulunduMu=True
            duzeltme=bilgiGir()
            i=0
            for d in duzeltme:
                if d!="":
                    liste[lst][i]=duzeltme[i]
                i+=1
            break
    if bulunduMu==False:
        input("Üzgünüm Aradığınız kişi bizde kayıtlı değil...")
    else:
        print("Kişi Düzeltildi...")

#kişi silmek için bu fonksiyon kullanılıyor. 
def kisiSilme(liste):
    aramaYap=arama(liste)
    bulunduMu=False
    for lst in aramaYap:
        print(liste[lst])
        sonuc=input("Silmek istediğiniz kayıt bu mu? (E/H)")
        if sonuc in "Ee":
            bulunduMu=True
            sonuc2=input("Kayıt silinecek Emin misiniz? (E/H)")
            if sonuc2 in "Ee":
                liste.remove(liste[lst])
                pass
            break
    if bulunduMu==False:
        input("Üzgünüm Aradığınız kişi bizde kayıtlı değil...")  
    else:
        print("Kişi Silindi...")

#menu bu fonksiyonda yazdırılır ve seçim return edilir. 
def menu():
    sonuc=""
    print("*"*5,"TELEFON REHBERİ PROGRAMINA HOŞGELDİNİZ","*"*5)
    print("1- Yeni Kişi Ekle")
    print("2- Kişi Arama")
    print("3- Kişi Düzenle")
    print("4- Kişi Sil")
    print("5- Tüm Kayıtları Listele")
    print("Q- Çıkış")
    
    while True:
        sonuc=input("Lütfen İşlemi Seçiniz :")
        if sonuc in "12345qQ":
            break    
        else:
            print("Lütfen menüdeki seçeneklerden birini seçiniz (1-4,Q)")
    return sonuc

#listelemek için bu fonksiyon kullanılıyor. 
def listeleme(liste):
    for araSonuc in liste:
        print(araSonuc)
    input("Kayıtların Sonu")




#ana İşlemlerin Yapıldığı Yer
rehber=[['Bilal', 'Canbulat', '06 85111111'], ['Fatma', 'Canbulat', '06 54553344']]
while True:
    islem=menu()
    if islem=="1":
        kisiEkle(rehber)
    elif islem=="2":
        kisiArama(rehber)
    elif islem=="3":
        kisiDuzeltme(rehber)
    elif islem=="4":
        kisiSilme(rehber)
    elif islem=="5":
        listeleme(rehber)
    elif islem in "Qq":
        break
    
