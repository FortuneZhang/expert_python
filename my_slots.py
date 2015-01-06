# codind=utf-8


class A(object):
    x = 1

    def __init__(self):
        self.y = 'y'


class B(object):

    __slots__ = ('x', 'y')

    def __init__(self):
        self.x = 10
        self.y = 100
        self.z = 1000

    def __setattr__(self, name, val):
        if name in B.__slots__:
            object.__setattr__(self, name, val)

    def __getattr__(self, name):
        return "Value of %s" % name


if __name__ == '__main__':
    a = A()
    print a.__dict__
    a.y = 10
    print a.__dict__

    print '----' * 8

    b = B()
    print b.__dict__
