class Protection:
    def __init__(self):
        self.protectedVar = 0

obj = Protection()
obj._protectedVar = 24
print(obj._protectedVar)

class Protecting:
    def __init__(self):
        self.__privateVar = 11

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protecting()
obj.getPrivate()
obj.setPrivate(22)
obj.getPrivate()
