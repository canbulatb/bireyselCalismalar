#soru 3: Kisinin adini, soyadini, adresini alip alt alta yazdiriniz. 
# Adresin altina adres kadar "*" ekleyiniz.

#Kullanıcıdan adını, soyadını ve adresini istiyoruz. 
adi=input("Lütfen adınızı giriniz...: ")
soyAdi=input("Lütfen soyadınızı giriniz...:")
adres=input("Lütfen adresinizi giriniz...: ")

#Kullanıcıdan aldığımız verileri alt alta yazdırıyoruz. 
print(adi,soyAdi,adres,"*"*len(adres),sep="\n")