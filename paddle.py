class Paddle:

    __height = 100
    __width = 10
    __x = 10
    __y = 175
    __yVel = 0
    __upVel = 0
    __downVel = 0
    __points = 0

    def getX(self):
        return self.__x

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def addPoint(self):
        self.__points += 1

    def getPoints(self):
        return self.__points

    def setY(self, value):
        self.__y = value

    def getY(self):
        return self.__y

    def setDownVel(self, value):
        self.__downVel = value

    def getDownVel(self):
        return self.__upVel

    def setUpVel(self, value):
        self.__upVel = value

    def getUpVel(self):
        return self.__upVel

    def getYVel(self):
        return self.__yVel

    def update(self):
        self.__yVel = self.__downVel - self.__upVel
        self.__y += self.__yVel
