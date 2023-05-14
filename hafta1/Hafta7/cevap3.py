# students.json adlı bir JSON dosyasında öğrenci bilgilerini saklayın. 
# Bu dosya, ad, soyad ve yaş bilgilerini içeren öğrenci nesnelerinden oluşan bir liste içermelidir. 
# Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# students.json dosyasını okuyun.
# Kullanıcıdan yeni bir öğrenci ekleme veya mevcut öğrencilerin listesini görüntüleme seçeneklerini sunun.
# Yeni öğrenci ekleme seçeneği seçilirse, kullanıcıdan öğrenci adı, soyadı ve yaşını isteyin ve JSON dosyasına ekleyin.
# Öğrenci listesini görüntüleme seçeneği seçilirse, öğrenci bilgilerini ekrana yazdırın.
# JSON dosyasını güncelleyin ve programı sonlandırın.

import json
import os
import sys
os.chdir((os.path.dirname(sys.argv[0]))) 

with open("students.json") as file:
    veri=json.load(file)

while True:
    while True:
        secenek=input("1-Yeni Öğrenci Ekle\n2-Ögrencileri Listele\nQ-Çıkış : ")
        if secenek in("12Qq") and len(secenek)==1:
            break
        else:
            print("Lütfen belirtilen seçenekleriden birini giriniz...:")
    if secenek in "Qq":
        break

    if secenek=="1":
        print("Lütfen öğrencinin")
        ad=input("Adını Giriniz...:")
        soyad=input("Soyadını Giriniz...:")
        yas=input("Yaşını Giriniz...:")
        ogrenci={"ad":ad,"soyad":soyad,"yas":yas}
        veri.append(ogrenci)
        with open("students.json", "w") as file:
            json.dump(veri, file)
        
    if secenek=="2":
            for x in veri:
                ogrenci=list(x.values())
                print("Öğrencinin Adı :",ogrenci[0])
                print("Öğrencinin Soyadı: ",ogrenci[1])
                print("Öğrencinin Yaşı",ogrenci[2])
                print("*"*30)
                
            