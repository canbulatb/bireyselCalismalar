# Bir metin dosyasında satır satır saklanan sayıların 
# toplamını ve ortalamasını hesaplayan bir program yazın. 
# Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# Kullanıcıdan dosya adı isteyin.
# Dosyayı okuyun ve satırlardaki sayıları toplayın.
# Toplam ve satır sayısını kullanarak ortalama değeri hesaplayın.
# Sonuçları ekrana yazdırın.
import os
import sys
os.chdir((os.path.dirname(sys.argv[0]))) 
dosyaAdi=input("Lütfen dosya adını giriniz...: ")
toplam=0
kacSayi=0


with open(dosyaAdi,"r") as file:
    for x in file:
        try:
            toplam+=int(x)
            kacSayi+=1
        except:
            pass
print("Ortalama",toplam/kacSayi)


    