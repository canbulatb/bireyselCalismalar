import random

def rollDice(sayi):
    zar=[0,0,0,0,0,0]
    zarYuzde=[]
    for i in range(0,sayi):
        rastgeleSayi=random.randint(0,5) #rastgele sayı oluşturuldu.
        zar[rastgeleSayi]=zar[rastgeleSayi]+1
    for zarDeger in zar:
        zarYuzde.append((zarDeger/sayi)*100)
    return zarYuzde
    