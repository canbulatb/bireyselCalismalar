# #Soru-1
# Bir dizi içeren bir liste verildiğinde, 
# listedeki tekrarlayan elemanlari bulan bir Python programı yazın. 
# Bu soruyu cozerken Python kumelerini kullanmaya calisin.

# Ornek Input:
# 1 2 3 4 12 45 1 2 54 65 77 8 1 2
# Ornek Output:
# Tekrarlayan öğeler: {1, 2}
print("********** 1. Sorunun Çözümü ******************")
liste=[1, 2, 3, 4, 12, 45, 1, 2, 54, 65, 77, 8, 1, 2]
set=set(liste[x] for x in range(len(liste)) if liste[x] in liste[x+1:] )
print(set)


