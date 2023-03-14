import keyword
yasakliKelimeler=keyword.kwlist
print(yasakliKelimeler)
print(len(yasakliKelimeler))

# print("""
# Burada 
#  birkaç satırlı
#   bir değişken
#    görüyorsunuz...
# """)

#print('Python programlama dilinin adı "piton" yılanından gelmez')


print("""
      
[H]==============HARMAN==========[-][O][X]
|                                        |
|     Programa Hoşgeldiniz!              |
|         Sürüm 0.8                      |
|    Devam etmek için herhangi           |
|        bir düğmeye basın.              |
|                                        |
|========================================|

""")



print("Python","Programlama","Dili")
print('Fenyx','Academy','Dronten',2018)
print("python"*2)


print(1,2,3,4,5, sep="-")

dosya=open("deneme.txt","w")
print("Ben Python, Monty Python", file=dosya)
dosya.close

print(*"Galatasaray", sep=".")

baslik="deneme"
print(baslik +"\n", "-"*len(baslik) , sep="")

sayi1=int(input("1. sayiyi giriniz"))
sayi2=int(input("2. sayiyi giriniz"))

print(sayi1+sayi2, sayi1-sayi2,sayi1*sayi2, sep="\n")

