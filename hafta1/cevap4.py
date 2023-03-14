#soru 4: Kullanicidan saniye alip gun, saat, dakika ve saniye olarak gosteriniz.

#Kullanıcıdan saniye girişi yapmasını istiyoruz. 
saniye=int(input("Hesaplanmasını istediğiniz saniye'yi giriniz...: "))

#Gün, saat ve dakikayı hesaplıyoruz. 
dakika=int(saniye/60)
saat=int(dakika/60)
gun=int(saat/24)

#hesapladığımız değerleri ekrana yazdırıyoruz. 
print("Girdiğiniz Değer ")
print("Gün    : "+ str(gun))
print("Saat   : "+ str(saat))
print("Dakika : "+ str(dakika))
print("Saniye : "+ str(saniye))
