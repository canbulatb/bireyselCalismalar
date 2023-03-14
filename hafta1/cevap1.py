#soru 1: Kullanicidan dairenin yaricapini alip dairenin alanini hesaplayiniz. 
# Dairenin alainin altini cizecek kadar "-" ekleyen program yaziniz.

# Kullanıcıdan dairenin yarıçapını istiyoruz. 
yariCap=int(input("Dairenin Yarıçapını Giriniz...:"))
#Pi sayısını tanıtıyoruz.
pi=3.14

#Dairenin alanını hesaplıyoruz
daireninAlani=int(pi*2*yariCap*yariCap)

#Ekrana dairenin alanını yazdırıyoruz. Kaçış karakteri kullanarak alt satıra iniyoruz ve yazdırdığımız yer kadar altını çizdiriyoruz. 
print(" Dairenin Alani : "+str(daireninAlani)+"\n", "-"*(len(str(daireninAlani))+17))
