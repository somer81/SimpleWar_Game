from os import system  # System kutuphanesi ekranlari temizleyebilmek icin cls
from random import randint  # rastgele sayi ureten sinif eklenir

class Silah:
    def __init__(self, isim:str, demage:int):
        self.__demage = demage
        self.__isim = isim

    def vur(self, rakip):  # Dusman yada oyuncu her kim vurulursa ondan can eksilir, vurma gucu 1 duser
        rakip.setCan(rakip.getCan() - self.__demage)
        self.__demage -= 1

    def getIsim(self):
        return self.__isim

    def getDemage(self):   # Mevcut kalan zarar verebilme gucunu gosterir
        return self.__demage

class Karakter:
    def __init__(self, can: int, silah: Silah):
        self.__can = can
        self.__silah = silah

    def vur(self,rakip):
        self.__silah.vur(rakip)

    def getCan(self):
        return self.__can

    def setCan(self, yeniCan:int):
        self.__can = yeniCan

    def getSilahIsim(self):
        return self.__silah.getIsim()

    def getDemage(self):
        return self.__silah.getDemage()

class Dusman(Karakter):
    pass

class Oyuncu(Karakter):
    #def __int__(self, isim:str, can:int, silah:Silah):
    #    super().__init__(can, silah)
        #self.__isim = isim

    def setIsim(self, isim:str):
        self.__isim = isim

    def getIsim(self):
        return self.__isim

def Main():
    dusmanlar = list() # dusmanlar icin bir dizi
    silahlar = ["Ok", "Tabanca", "Roket"]  # {"Ok":10, "Tabanca":20, "Roket":100}  silahlar["Ok"]
    s = {"Ok":randint(0,10), "Tabanca":randint(20,30), "Roket":randint(30,50)} # Dictionary
    silah_list = list(s)
    silah_sec = silah_list[randint(0,len(silah_list)-1)]
    #print(silah_list[0], str(silah_list[0]))  # sozluk icinde silah ismi ve vurus gucu alabilrim

    for i in range(5):
        silah_sec = silah_list[randint(0, len(silah_list) - 1)]
        #dusmanlar.append(Dusman(randint(20, 40), Silah(silahlar[randint(0,len(silahlar)-1)], randint(10, 20))))
        dusmanlar.append(Dusman(randint(20, 40), Silah(str(silah_sec), s[str(silah_sec)])))
    oyuncu = Oyuncu(80, Silah("Tabanca", 45))
    oyuncu.setIsim("Omer")
    #oyuncu = Oyuncu()
    while True:
        system("cls")  # python kodu icersinden konsolu temizler
        print("Oyuncu {}    ----    Can {}    ----    Silah {}    ----    Demage {}".format(oyuncu.getIsim(), oyuncu.getCan(), oyuncu.getSilahIsim(), oyuncu.getDemage()))
        print("=============================================================================")

        for num, i in enumerate(dusmanlar):
            print("No {}  Can {}    ----    Demage {}    ----    Silah {}".format(num, i.getCan(), i.getDemage(), i.getSilahIsim()))

        secim = input("Saldirilacak Dusmani Seciniz : ")
        dusman = dusmanlar[int(secim)]
        oyuncu.vur(dusman)
        if dusman.getCan() <= 0:
            dusmanlar.remove(dusman)
            if not dusmanlar:  # eger dusmanlar listesinde hic dusman kalmamissa
                print("You Win!")
                break

        if dusmanlar:
            dusmanlar[randint(0, len(dusmanlar)-1)].vur(oyuncu)
            if oyuncu.getCan() <= 0:
                print("Game Over")
                break

if __name__ == "__main__":
    Main()





