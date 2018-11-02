import re
#from re import *

pattern = r'(\w+):(\d+)'
s = 'zhang:1998 li:1996'
a = re.findall(pattern,s,flags = 0)
print('a=',a)


regex = re.compile(pattern,flags = 0)
b = regex.findall(s,pos = 0,endpos = 12)
print('b=',b)



c = re.split(r'\s+','hello world')
print(c)