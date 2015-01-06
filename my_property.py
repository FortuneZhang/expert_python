# coding=utf-8


class C(object):

    def __init__(self):
        self.x = None

    def getx(self):
        print 'get x'
        return self._x

    def setx(self, value):
        print 'set x'
        self._x = value

    def delx(self):
        print 'del x'
        del self._x

    x = property(getx, setx, delx, 'I\'m x ')


if __name__ == '__main__':
    c = C()
    c.x = 10
    print c.x
   
