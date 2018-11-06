import random

class Ball:
    __radius = 10
    __x = 295
    __y = 245
    __xVel = 0
    __yVel = 0

    def setRandomVel(self):
        '''
        self.__xVel = random.randint(-10, 10)
        self.__yVel = random.randint(-10, 10)

        if(self.__xVel == 0 or self.__yVel == 0):
            self.setRandomVel()
        '''
        self.__xVel = 1
        self.__yVel = .5

        if(random.randint(-1, 1) > 0):
            self.__xVel *= -1
        if(random.randint(-1, 1) > 0):
            self.__yVel *= -1


    def __init__(self):
        self.setRandomVel()

    def getRadius(self):
        return self.__radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getYVel(self):
        return self.__yVel

    def getXVel(self):
        return self.__xVel

    def setX(self, value):
        self.__x = value

    def setY(self, value):
        self.__y = value

    def setYVel(self, value):
        self.__yVel = value

    def setXVel(self, value):
        self.__xVel = value

    def update(self):
        self.__x += self.__xVel
        self.__y += self.__yVel
