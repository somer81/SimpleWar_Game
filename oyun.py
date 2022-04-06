from os import system
from random import randint

class Silah:
    def __init__(self, isim:str, demage:int):
        self.__demage = demage
        self.__isim = isim

    def vur(self, rakip):
        rakip.setCan(rakip.getCan() - self.__demage)
        self.__demage -= 1

    def getIsim(self):
        return self.__isim

    def getDemage(self):
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
    #def __int__(self, can:int, silah:Silah):
    #    super().__init__(can, silah)
        #self.__isim = isim

    def getIsim(self):
        return "Omer"



def Main():
    dusmanlar = list()
    for i in range(10):
        dusmanlar.append(Dusman(randint(30, 50), Silah("Ok", randint(10, 20))))
    oyuncu = Oyuncu(120, Silah("Tabanca", 25))
    #oyuncu = Oyuncu()
    while True:
        system("cls")
        print("Oyuncu {}    ----    Can {}    ----    Silah {}    ----    Demage {}".format(oyuncu.getIsim(), oyuncu.getCan(), oyuncu.getSilahIsim(), oyuncu.getDemage()))
        print("=============================================================================")

        for num, i in enumerate(dusmanlar):
            print("No {}  Can {}    ----    Demage {}    ----    Silah {}".format(num, i.getCan(), i.getDemage(), i.getSilahIsim()))

        secim = input("Saldirilacak Dusmani Seciniz : ")
        dusman = dusmanlar[int(secim)]
        oyuncu.vur(dusman)
        if dusman.getCan() <= 0:
            dusmanlar.remove(dusman)
            if not dusmanlar:
                print("You Win!")
                break

        if dusmanlar:
            dusmanlar[randint(0, len(dusmanlar)-1)].vur(oyuncu)
            if oyuncu.getCan() <= 0:
                print("Game Over")
                break


if __name__ == "__main__":
    Main()




