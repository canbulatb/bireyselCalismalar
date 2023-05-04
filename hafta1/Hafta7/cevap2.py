#Bir metin dosyasındaki her satırın başına 
# satır numarası ekleyen bir program yazın. 
# Programınız aşağıdaki işlemleri gerçekleştirmelidir:

# Kullanıcıdan dosya adı isteyin.
# Dosyayı okuyun ve her satırın başına satır numarası ekleyin.
# Dosyayı güncellenmiş içerikle tekrar yazın.
import os
import sys
dosyaAdi=input("Lütfen dosya adını giriniz...: ")
os.chdir((os.path.dirname(sys.argv[0]))) 
say=1
with open(dosyaAdi,"r") as file:
    yeniDosya=file.readlines()
file=open(dosyaAdi,"w")
for x in yeniDosya:
    file.write(str(say)+"-"+x)
    say+=1
file.close()