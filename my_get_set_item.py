# coding=utf-8


class C(object):

    def __init__(self):
    	self.rex = {}

    def __setitem__(self,key,value):
    	self.rex[key] = value

    def __getitem__(self,key):
    	if self.rex.has_key(key):
    		return self.rex[key]
    	else:
    		return None

if __name__ == '__main__':
	c = C()
	c['x']  = 'x'
	c['y'] = 'y'

	print 'x->', c['x']
	print 'y->', c['y']

	print 'z->', c['z']
