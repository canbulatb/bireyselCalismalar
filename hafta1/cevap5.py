#soru 5: Kullanicidan ismini ve soy ismini alip bir dikdortgenin 
#ortasina yazidiran bir program yaziniz.
#(Isim ve Soysisim uzunluguna gore dikdortgen buyuyup kuculmelidir.)

#Kullanıcıdan isim ve soyismi girmesini istiyoruz. 
adiSoyadi=input("Lütfen Adınızı ve Soyadınızı Giriniz....: ")
#adı soyadını bir kutu içerisinde yazdırıyoruz.    
print("\n|"+"="*(len(adiSoyadi)+6)+"|")
print("|"+"*"*3 + adiSoyadi+ "*"*3+"|")
print("|"+"="*(len(adiSoyadi)+6)+"|")
