#coding=utf-8

f = open('./file_change.md')
for x in f.readlines():
	print x 
f.close()

f = open('./file_change.md', 'w')
f.seek(3)
f.write('3')
f.close()

f = open('./file_change.md')
for x in f.readlines():
	print x 
f.close()
