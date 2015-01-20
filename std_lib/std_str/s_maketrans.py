#codind=utf-8
import string

leet = string.maketrans('abct', '1230')
s = 'the quick brown fox jumped over the lazy dog.t'
print s
print s.translate(leet)

s.replace('t','T')
print s
print s.replace('t','T')
