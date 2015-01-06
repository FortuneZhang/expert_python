# codind=utf-8
class C(object):

    def __init__(self):
        self._height = 100

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

if __name__ == '__main__':
    c = C()
    print c.height
    # print c.height() error height not function is property
    c.height = 200
    print c.height
