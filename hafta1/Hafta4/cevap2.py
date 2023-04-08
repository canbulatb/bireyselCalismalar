# Soru-2
# Bir restoranın menüsünü Python sözlükleri kullanarak oluşturun 
# ve kullanıcının yemekler sipariş etmesine izin verin.

# Aşağıdaki adımları izleyebilirsiniz:
# Restoranın menüsünü bir Python sözlüğü olarak oluşturun.
# Her yemek bir anahtar kelime, fiyatı ise değer olarak tanımlanabilir.
# Kullanıcının menüyü görmesi için menüyü ekrana yazdırın.
# Kullanıcıdan yemekler sipariş etmesini isteyin. 
# Kullanıcı, bir yemek adı veya numarası girebilir.
# Kullanıcının seçtiği yemekleri bir sözlükte saklayın.
# Kullanıcının siparişlerini ekrana yazdırın ve toplam fiyatı hesaplayın.
print("********** 2. Sorunun Çözümü ******************")
menuSozluk={"Adana Kebab":20,"Tavuk Kanat":15,"Çorba":5,"Ayran":2}
menuListe=[key for key in menuSozluk.keys()]
SiparisListe=[]
siparis=0
while True:
    print("Menü")
    i=0
    for key,value in menuSozluk.items():
        print(f"{i+1} - {key}\t: {value} TL ")
        i+=1
    siparis=int(input("lütfen siparişinizi giriniz...: (çıkış 0) "))
    while True:
        if siparis>len(menuListe):
            print("Lütfen Listeden birini seçiniz..." )
        else:
            if siparis!=0:
                SiparisListe.append(menuListe[siparis-1])
            break
    if siparis==0:
        break
print(SiparisListe)
toplam=0
for hesap in SiparisListe:
    toplam+=int(menuSozluk[hesap])

print("Hesabınız...: ", toplam)