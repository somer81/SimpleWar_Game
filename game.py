class Gun:
    def __int__(self, name:str, demage:int):
        self.__name = name
        self.__demage = demage

    def hit(self, rival):
        rival.setLife(rival.getLife() - self.__demage)
        self.__demage -= 1

    def getName(self):
        return self.__name

    def getDemage(self):
        return self.__demage

class GameChar:
    def __int__(self, life:int, gun:Gun):
        self.__life = life
        self.__gun = gun

    def getLife(self):
        return  self.__life

    def setLife(self, val:int):
        self.__life = val

    def getGunName(self):
        self.__gun.getName()

    def getDemage(self):
        self.__gun.getDemage()

class GamePlayer(GameChar):
    pass

class GameEnemy(GameChar):
    pass

