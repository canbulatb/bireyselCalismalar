#Zar adlı 6 öğeli bir liste oluşturun. Bu listeyi sıfır değeriyle doldurun. 
# 5000 kez tekrarlayarak 1 ile 6 arasında (tıpkı bir zar gibi) rastgele bir sayı oluşturun.
#Değer 1 ise, listedeki 0 öğesini 1 artırın, aynısı 2, 3, 4, 5 ve 6 değerleri için de geçerlidir. 
# dice[0] öğesi, 1 değerinin kaç kez oluştuğunu gösterir. 
# Veya genel olarak: zar[x-1], x'in kaç kez atıldığını gösterir.

#Tekrarın sonunda, listenin içeriğini 2 ondalık basamakla yüzde olarak yazdırın.
# Örneğin; "3 değerindeki atışların yüzdesi = %16,28"
import random
zar=[0,0,0,0,0,0]
for i in range(0,5000):
    rastgeleSayi=random.randint(0,5) #rastgele sayı oluşturuldu.
    zar[rastgeleSayi]=zar[rastgeleSayi]+1
j=1
for zarDeger in  zar:
    print(f"zarda {j}, {zarDeger} kez atıldı. %{(zarDeger/50):.2f}")
    j+=1
    