#1'den 100'e kadar rastgele bir tam sayı seçen bir program yazınız. 
# Programınız kullanıcıdan tahminler istemelidir – eğer kullanıcı 
# yanlış tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdırmalıdır. 
# Kullanıcı doğru tahmin ederse, program kullanıcının doğru cevabı tahmin etmek 
# için ne kadar zaman harcadığını yazdırmalıdır. 
# Kullanıcının geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.
import time
import random
seconds1 = time.time() #programa başlama saniyesini değişkene aktarıldı.
rastgeleSayi=random.randint(0,100) #rastgele sayı oluşturuldu.
ustSayi=100 #Tahmin oyunu için üst sınır
altSayi=1   #tahmin oyunu için alt sınır
tahminSayisi=0 #tahmin kaçıncı defada doğru bilinmesi için oluşturulan değişken. 
while True:
    try:
        #Kullanıcıdan değer girmesini istiyoruz. 
        kullaniciSayi=input(f"Lütfen {altSayi}-{ustSayi} arasında bir tam sayı giriniz. (Çıkmak için Q) ")
        #girilen değer integer e dönüştürülürken hata verirsek except kısmından kontroller yapılıyor.
        # Hata vermesse program devam ediyor. 
        kullaniciSayiInt=int(kullaniciSayi)
        #sadece sayı girildiği artık kesin.
        # Kullanıcı bizim belirlediğimiz değerin üstünde veya altında giriş yaparsa hata fırlatıyoruz.
        if kullaniciSayiInt>ustSayi or kullaniciSayiInt<altSayi :
             raise ValueError
        #hata yok o yüzden tahmin sayısını bir arttırıyoruz.
        tahminSayisi+=1
        #kullanıcının tahminlerini değerlendiriyoruz. 
        # Eğer doğruysa kaç defada ve kaç saniyede bildiğini ekrana yazdırıyoruz.
        if kullaniciSayiInt==rastgeleSayi:
            seconds2=time.time()
            print(f"{tahminSayisi} Seferde bildin. Bravo...")
            print(f"{int(seconds2-seconds1)} saniyede tahmin ettin.") 
            break
        #Eğer kullanıcı tahmini yanlışsa Büyük veya küçük girmesini belirtiyoruz.
        # üst ve alt limitleri kullanıcının girdiği değere göre güncelliyoruz. 
        elif kullaniciSayiInt>rastgeleSayi:
            print("Daha küçük bir sayı tahmininde bulun...")
            ustSayi=kullaniciSayiInt
        elif kullaniciSayiInt<rastgeleSayi:
            print("Daha büyük bir sayı tahmininde bulun...")
            altSayi=kullaniciSayiInt
    #hata varsa
    #Kullanıcı çıkış yapmak istemiş ise "break" ile while döngüsünden çıkış yaptırıyoruz. 
    # yoksa hatalı giriş yaptığını belirtip programa devam ediyoruz.  
    except ValueError :
        if kullaniciSayi in ("Qq"):
            print("Oyun bitmedi ama işin çıktı heralde. Müsait olduğunda tekrar bekleriz.")
            break
        print("Yanlış giriş yaptınız. Lütfen yeniden deneyiniz...") 
    
        
            
    
    

