import my_dice

while True:
    try:
        tekrarNo= input("Tekrar numarasını girin: (Çıkış Q)")
        tekrarNoInt=int(tekrarNo)
        sonuc=my_dice.rollDice(tekrarNoInt)
        j=1
        for sonucYaz in sonuc:
           print(f"zar {j}, %{(sonucYaz):.2f}")
           j+=1
    except ValueError :
        if tekrarNo in ("Qq"):
            break
        print("Yanlış giriş yaptınız. Lütfen yeniden deneyiniz...") 