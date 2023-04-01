sayilar = [[0, 10], [6, 60], [12, 54], [67, 99]]
for i in sayilar:
    print(*range(*i)) #* ne işe yarıyordu...


alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harfListesi=list(alfabe)
print(harfListesi)

isimler = "elma, armut, çilek"
isim=isimler.split(", ")
print(isim)